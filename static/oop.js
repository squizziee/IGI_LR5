
class TaskBase {
    static ownerIdCounter = 1
    static sectorIdCounter = 1

    constructor(owners, sectors) {
        this.owners = []
        owners.forEach(owner => {
            owner.id = TaskBase.ownerIdCounter++
            this.owners.push(owner)
        })

        this.sectors = []
        sectors.forEach(sector => {
            sector.id = TaskBase.sectorIdCounter++
            this.sectors.push(sector)
        })
    }

    addOwner(name) {
        let newOwner = new Owner(name)
        newOwner.id = TaskBase.ownerIdCounter++
        this.owners.push(newOwner)
    }

    setOwners(owners) {
        this.owners = []
        owners.forEach(owner => {
            owner.id = TaskBase.ownerIdCounter++
            this.owners.push(owner)
        })
    }

    getOwners() {
        return this.owners
    }

    addSector(area, ownerId) {
        let newSector = new Sector(area, ownerId)
        newSector.id = TaskBase.sectorIdCounter++
        this.sectors.push(newSector)
    }

    setSectors(sectors) {
        this.sectors = []
        sectors.forEach(sector => {
            sector.id = TaskBase.sectorIdCounter++
            this.sectors.push(sector)
        })
    }

    getSectors() {
        return this.sectors
    }
}

function Owner(name) {
    this.name = name;
    this.id = -1
}

function Sector(area, ownerId) {
    this.id = -1
    this.area = area;
    this.ownerId = ownerId
}

class TaskCore extends TaskBase {
    findOwnersSectors(ownerId) {
        let result = [];
        this.sectors.forEach(sector => {
            if (sector.ownerId === ownerId) {
                result.push(sector);
            }
        })
        return result;
    }

    findOwnersWithMultipleSectors() {
        let result = [];
        this.owners.forEach(owner => {
            let sectors = this.findOwnersSectors(owner.id)
            if (sectors.length > 1) {
                result.push(owner);
            }
        })
        return result;
    }

    calculateOwnersTotalSectorArea(ownerId) {
        let sectors = this.findOwnersSectors(ownerId);
        let total = 0.0;
        sectors.forEach(sector => {
            total += sector.area
        })
        return total;
    }

    renderAllOwners() {
        let renderArea = document.querySelector('#owners')
        renderArea.innerHTML = ''
        this.owners.forEach(owner => {
            let element = document.createElement('div')
            element.innerText = `${owner.name}, id = ${owner.id}`
            renderArea.appendChild(element)
        })
    }

    renderAllSectors() {
        let renderArea = document.querySelector('#sectors')
        renderArea.innerHTML = ''
        this.sectors.forEach(sector => {
            let element = document.createElement('div')
            element.innerText = `Owner id: ${sector.ownerId}, area = ${sector.area} sq. m., id = ${sector.id}`
            renderArea.appendChild(element)
        })
    }

    performTaskAndRenderResult() {
        let renderArea = document.querySelector('#result')
        renderArea.setAttribute('style', 'white-space: pre;');
        renderArea.innerHTML = ''
        let step1 = this.findOwnersWithMultipleSectors()
        step1.forEach(owner => {
            let element = document.createElement('div')
            element.textContent = ''
            element.textContent += `Owner ${owner.name}: \n`
            let step2 = this.findOwnersSectors(owner.id)
            step2.forEach(sector => {
                element.textContent += `-> Sector ${sector.id}, area: ${sector.area}\n`
            })
            let step3 = this.calculateOwnersTotalSectorArea(owner.id)
            element.textContent += `-----> Total area: ${step3}`

            renderArea.appendChild(element)
        })
    }
}

let owners = [
    new Owner('Ivan'),
    new Owner('Egor'),
    new Owner('Danik'),
    new Owner('Slava'),
    new Owner('Ilia'),
];

let sectors = [
    new Sector(25.0, 1),
    new Sector( 4.0, 1),
    new Sector( 255.0, 2),
    new Sector( 1.0, 2),
    new Sector( 13.0, 2),
    new Sector( 22.1, 3),
    new Sector( 21.0, 4),
    new Sector( 2100.0, 5),
    new Sector( 0.05, 5),
]
let task = new TaskCore(owners, sectors);
let ownerForm = document.forms['owner_form'];
let sectorForm = document.forms['sector_form'];

ownerForm.addEventListener('submit', e => {
    e.preventDefault();
    const data = new FormData(ownerForm);
    task.addOwner(data.get('name'))
    task.renderAllOwners()
    task.performTaskAndRenderResult()
})

sectorForm.addEventListener('submit', e => {
    e.preventDefault();
    const data = new FormData(sectorForm);
    let area = Number(data.get('area'))
    let ownerId = Number(data.get('owner_id'))
    if (ownerId > TaskBase.ownerIdCounter - 1 || ownerId < 1) {
        alert('Wrong owner id');
        return;
    }
    if (area <= 0.00000001) {
        alert('Area too small');
        return;
    }
    task.addSector(area, ownerId)
    task.renderAllSectors()
    task.performTaskAndRenderResult();
})

task.renderAllOwners()
task.renderAllSectors()

task.performTaskAndRenderResult()