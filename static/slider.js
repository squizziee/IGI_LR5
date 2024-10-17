
let slider = document.querySelector(".slider");
let slider_counter = slider.querySelector(".slider_counter");
let prev_ctrl = slider.querySelector(".prev");
let next_ctrl = slider.querySelector(".next");
let slides = slider.querySelectorAll('.slider_image');
let current_slide_index = 0;
let captions = slider.querySelectorAll(".slider_image_caption");
let pagination = slider.querySelector(".slider_pagination");
let pagination_items = pagination.querySelectorAll(".slider_pagination_item");

let slider_config = {
    'loop': slider.getAttribute('loop') !== null,
    'navs': slider.getAttribute('navs') !== null,
    'pagination': slider.getAttribute('pagination') !== null,
    'auto': slider.getAttribute('auto') !== null,
    'pause_on_hover': slider.getAttribute('pauseonhover') !== null,
    'delay': slider.getAttribute('delay'),
}

console.log(slider_config)

let interval_id = null;

setup_initial();
setup_controls();
setup_auto_rotation();
setup_hover_behaviour()

// functions
function switch_slides(index) {
    slides[current_slide_index].classList.remove('active');
    pagination_items[current_slide_index].classList.remove('active');
    captions[current_slide_index].classList.remove('active');

    current_slide_index = index;
    slides[index].classList.add('active');
    update_slider_counter();
    update_pagination();
    update_captions();
}

function update_slider_counter() {
    slider_counter.innerHTML = `${current_slide_index + 1} / ${slides.length}`
}

function update_pagination() {
    pagination_items[current_slide_index].classList.add('active');
}

function update_captions() {
    captions[current_slide_index].classList.add('active');
}

// setup functions
function setup_initial() {
    slides[0].classList.add('active')
    captions[0].classList.add('active')
    pagination_items[0].classList.add('active')
    update_slider_counter();

    for (let i = 0; i < pagination_items.length; i++) {
        pagination_items[i].addEventListener('click', () => {
            switch_slides(i)
        })
    }

    prev_ctrl.addEventListener('click', () => {
        if (current_slide_index === 0) {
            if (slider_config['loop']) {
                switch_slides(slides.length - 1);
            }
        } else {
            switch_slides(current_slide_index - 1)
        }
    });

    next_ctrl.addEventListener('click', () => {
        if (current_slide_index === slides.length - 1) {
            if (slider_config['loop']) {
                switch_slides(0);
            }
        } else {
            switch_slides(current_slide_index + 1)
        }
    });
}

function setup_controls() {
    if (slider_config['navs']) {
        prev_ctrl.classList.add('enabled');
        next_ctrl.classList.add('enabled');
    }
    if (slider_config['pagination']) {
        pagination.classList.add('enabled')
    }
}

function setup_auto_rotation() {
    if (slider_config['auto']) {
        let delay = slider_config['delay'] === null ? 5000 : slider_config['delay']
        interval_id = setInterval(() => {
            if (current_slide_index === slides.length - 1) {
                switch_slides(0)
            } else {
                switch_slides(current_slide_index + 1);
            }
        }, delay)
    }
}

function setup_hover_behaviour() {
    if (slider_config['pause_on_hover']) {
        slider.addEventListener('mouseover', () => {
            clearInterval(interval_id);
        })
        slider.addEventListener('mouseout', () => {
            setup_auto_rotation();
        })
    }
}