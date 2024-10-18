let wrapper = document.querySelector('#table_wrapper')
let table = document.querySelector('#management_table');
let table_head = Array.from(table.rows)[0];
// all info loaded from server
let readonly_rows = Array.from(table.rows).slice(1);
// all info not divided by pages
let all_rows = Array.from(table.rows).slice(1);

console.log(readonly_rows)

const page_size = 3;
let current_page = 0;

// content of one page
let rows = all_rows.slice(page_size * current_page, page_size * current_page + page_size);
take_slice(0);

console.log(rows)

let sorted_by_name = {'value': null};
let sorted_by_experience = {'value': null};
let sorted_by_email = {'value': null};
let sorted_by_speciality = {'value': null};

function take_slice(page_number) {
    current_page = page_number;
    rows = all_rows.slice(page_size * current_page, page_size * current_page + page_size);
     while (table.rows.length > 1) {
        table.deleteRow(1);
    }
    rows.forEach(row => table.tBodies[0].appendChild(row));
     create_pagination();
}

function create_pagination() {
    let pagination_try_get = wrapper.querySelector("#pagination")
    let total_pages = Math.ceil(all_rows.length / page_size)
    let pagination = null;

    if (pagination_try_get == null) {
        pagination = document.createElement("div")
    } else {
        pagination = pagination_try_get;
        pagination.innerHTML = ""
    }

    pagination.id = 'pagination'
    for (let i = 0; i < total_pages; i++) {
        let btn = document.createElement("button")
        let text = document.createTextNode(`${i}`)
        btn.appendChild(text);
        btn.setAttribute('onclick', `take_slice(${i})`)
        pagination.appendChild(btn);
    }
    wrapper.appendChild(pagination )
}

function sort_outer(metric_id) {
    switch (metric_id) {
        case 1:
            manage_sort_direction(1, sorted_by_name, false, "Name");
            return;
        case 2:
            manage_sort_direction(2, sorted_by_experience, true, "Experience");
            return;
        case 3:
            manage_sort_direction(3, sorted_by_email, false, "Email");
            return;
        case 4:
            manage_sort_direction(4, sorted_by_speciality, false, "Speciality");
            return;
    }
}

function update_sort_info(metric_id, text, full_reset = false) {
    for (let i = 0; i < table_head.cells.length; i++) {
        table_head.cells[i].innerText =
            table_head.cells[i].innerText.split('(')[0]
    }
    if (!full_reset) table_head.cells[metric_id].innerText = text;
}

function manage_sort_direction(metric_id, sort_status, is_numeric=false, column_text) {
    let sorted = null;
    if (sort_status.value == null) {
        sorted = sort_by(metric_id, is_numeric);
        sort_status.value  = 1;
        update_sort_info(metric_id, column_text + "(asc)")
    } else if (sort_status.value  === 1) {
        sorted = sort_by(metric_id, is_numeric);
        sorted.reverse();
        sort_status.value  = -1;
        update_sort_info(metric_id, column_text + "(desc)")
    } else if (sort_status.value  === -1) {
        sorted = sort_by(metric_id, is_numeric);
        sort_status.value  = 1;
        update_sort_info(metric_id, column_text + "(asc)")
    }
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }
    sorted.forEach(row => table.tBodies[0].appendChild(row));
    take_slice(current_page);
}

function sort_by(metric_id, is_numeric=false) {
    return all_rows.sort((row1, row2) => {
        let content1 = row1.cells[metric_id].getAttribute("data-content");
        let content2 = row2.cells[metric_id].getAttribute("data-content");

        if (is_numeric) {
            content1 = Number(content1)
            content2 = Number(content2)
        }

        if (content1 < content2) return -1;
        else if (content1 > content2) return 1;
        return 0;
    });
}

// search
let search = document.querySelector('#search');
let submit_btn = search.querySelector('#submit');

submit_btn.addEventListener('click', () => {
   search_substring();
});

function search_substring() {
    let column_id = Number(search.querySelector('#column_id').value);
    let query = search.querySelector('#query').value;
    let filtered_rows = [];

    // while (table.rows.length > 1) {
    //     table.deleteRow(1);
    // }
    all_rows = []
    readonly_rows.forEach(row => {
        let content = row.cells[column_id].getAttribute("data-content")
        if (column_id === 4) {
            content = row.cells[column_id].innerText
        }
        content = content.toLowerCase()
        let regex = new RegExp(`${query}`)
        if (regex.test(content)) {
            all_rows.push(row)
            //table.tBodies[0].appendChild(row);
        }
    });
    update_sort_info(null, null, true)
    take_slice(0);
}

// info showoff
async function show_info(master_id) {
    showPreloader();
    let data = null;
    fetch(`/masters/${master_id}`)
        .then(response => response.json())
        .then(response_data => {
            data = JSON.parse(response_data)
            hidePreloader();
        }
    ).then(
        _ => {
            let card = wrapper.querySelector('#info');
            card.innerHTML = ""

            let image = document.createElement('img')
            image.src = data.image_url;
            card.appendChild(image);

            let general_info = document.createElement('article');
            general_info.innerText = `Name: ${data.name}, Experience: ${data.experience}, Email: ${data.email}`
            card.appendChild(general_info)

            let dividing_text = document.createElement('strong');
            dividing_text.innerText = 'Services: '
            card.appendChild(dividing_text)

            for (let i = 0; i < data.speciality.services.length; i++) {
                let service = data.speciality.services[i];
                let service_info = document.createElement('article');
                card.appendChild(service_info);
                service_info.innerText = "";
                service_info.innerText += `Name: ${service.service_name}, Description: ${service.service_description}, Base price: \$${service.service_price}`
            }
        }
    )
    //data = JSON.parse(await (await fetch(`/masters/${master_id}`)).json())


}

// master addition
function validate_form() {
    console.log("changed")
    let form = document.forms['add_master_form'];
    let error_message_area = document.querySelector('.error_message')
    let submit_btn = form["submit"];
    error_message_area.innerText = ''

    let phone = form['phone_number'].value;
    let avatar_url = form['avatar_url'].value;

    form['phone_number'].classList.remove('invalid')
    form['avatar_url'].classList.remove('invalid')

    let valid = true;

    let phone_pattern = new RegExp('(\\+375|8)( ?\\(?0?\\d\\d\\)? ?)((\\d\\d\\d-\\d\\d-\\d\\d)|(\\d\\d\\d\\d\\d\\d\\d)|(\\d\\d\\d \\d\\d \\d\\d))')
    if (!phone_pattern.test(phone) || phone.length < 11) {
        error_message_area.innerText += 'Wrong phone number format'
        form['phone_number'].classList.remove('invalid')
        form['phone_number'].classList.add('invalid')
        valid = false;
    }

    let url_pattern = new RegExp('https:\\/\\/.+\\/.+\\.(jpg|png)')
    if (!url_pattern.test(avatar_url)) {
        if (!valid) error_message_area.innerText += ', wrong url format'
        else error_message_area.innerText += 'Wrong url format'
        form['avatar_url'].classList.remove('invalid')
        form['avatar_url'].classList.add('invalid')
        valid = false
    }

    if (valid) submit_btn.removeAttribute('disabled');
}

// preloader
function showPreloader() {
    let preloader = document.querySelector('.preloader_container');
    console.log("Preloader shown")
    preloader.classList.remove('ready');
    setTimeout(() => {}, 1000)
}

function hidePreloader() {
    let preloader = document.querySelector('.preloader_container');
    console.log("Preloader removed")
    preloader.classList.add('ready');
}

// award
let award_btn = document.querySelector('#award_btn');

function award_selected() {
    let selected_rows = []
    all_rows.forEach(row => {
        let checked = row.cells[6].querySelector('input').checked
        if (checked) {
            selected_rows.push(row)
        }
    })

    let awarded_section = document.querySelector("#awarded_masters")
    awarded_section.innerHTML = ''
    let heading = document.createElement('h1')
    heading.innerText = "Awarded"
    awarded_section.appendChild(heading);

    selected_rows.forEach(row => {
        let text = document.createElement('div')
        text.innerText = row.cells[1].innerText
        awarded_section.appendChild(text)
    })
}