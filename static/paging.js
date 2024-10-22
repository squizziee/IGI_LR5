let wrapper = document.querySelector('.service_wrapper')
let readonly_items = [...wrapper.querySelectorAll('.card_wrapper')]
let items = readonly_items;

readonly_items.forEach(
    card_w => {
        const card = card_w.querySelector(".service_item");

        card_w.addEventListener('mousemove', event=>{
            //console.log(card_w.getBoundingClientRect());
            const [x, y] = [event.offsetX, event.offsetY];
            const rect = card_w.getBoundingClientRect();
            const [width, height] = [rect.width, rect.height];
            const middleX = width / 2;
            const middleY = height / 2;
            const offsetX = ((x - middleX) / middleX) * 25;
            const offsetY = ((y - middleY) / middleY) * 25;
            const offX = 50 + ((x - middleX) / middleX) * 25;
            const offY = 50 - ((y - middleY) / middleY) * 20;
            card.style.setProperty("--rotateX", 1 * offsetX + "deg");
            card.style.setProperty("--rotateY", -1 * offsetY + "deg");
            card.style.setProperty("--posx", offX + "%");
            card.style.setProperty("--posy", offY + "%");
        });
        card_w.addEventListener('mouseleave', eve=>{

            card.style.animation = 'reset-card 1s ease';
            card.addEventListener("animationend", e=>{
                card.style.animation = 'unset';
                card.style.setProperty("--rotateX", "0deg");
                card.style.setProperty("--rotateY", "0deg");
                card.style.setProperty("--posx", "50%");
                card.style.setProperty("--posy", "50%");
            }, {
                once: true
            });
        });
    });

const page_size = 3;
let current_page = 0

take_slice(current_page)

function take_slice(page_number) {
    current_page = page_number;
    items = readonly_items.slice(page_size * current_page, page_size * current_page + page_size);
    wrapper.innerHTML = ''
    items.forEach(card => wrapper.appendChild(card));
    update_pagination();
}

function update_pagination() {
    let total_pages = Math.ceil(readonly_items.length / page_size)
    let pagination = document.querySelector(".pagination")
    pagination.innerHTML = ""
    for (let i = 0; i < total_pages; i++) {
        let btn = document.createElement("button")
        btn.classList.add('btn_general')
        let text = document.createTextNode(`${i}`)
        btn.appendChild(text);
        btn.setAttribute('onclick', `take_slice(${i})`)
        pagination.appendChild(btn);
    }
}