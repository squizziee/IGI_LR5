
class Slider {
    #slider = null
    #slider_counter = null
    #prev_ctrl = null
    #next_ctrl = null
    #slides = null
    #current_slide_index = 0;
    #captions = null
    #pagination = null
    #pagination_items = null
    #config = {}

    #interval_id = null

    constructor(components) {
        this.#slider = components['slider']
        this.#slider_counter = components['slider_counter']
        this.#prev_ctrl = components['prev_ctrl']
        this.#next_ctrl = components['next_ctrl']
        this.#slides = components['slides']
        this.#current_slide_index = 0;
        this.#captions = components['captions']
        this.#pagination = components['pagination']
        this.#pagination_items = components['pagination_items']

        this.#config = {
            'loop': this.#slider.getAttribute('loop') !== null,
            'navs': this.#slider.getAttribute('navs') !== null,
            'pagination': this.#slider.getAttribute('pagination') !== null,
            'auto': this.#slider.getAttribute('auto') !== null,
            'pause_on_hover': this.#slider.getAttribute('pauseonhover') !== null,
            'delay': this.#slider.getAttribute('delay'),
        }

        this.#setup()
    }

    #setup() {
        this.#setup_initial()
        this.#setup_controls()
        this.#setup_auto_rotation()
        this.#setup_hover_behaviour()
    }

    #setup_initial() {
        this.#slides[0].classList.add('active')
        this.#captions[0].classList.add('active')
        this.#pagination_items[0].classList.add('active')
        this.#update_slider_counter();

        for (let i = 0; i < this.#pagination_items.length; i++) {
            this.#pagination_items[i].addEventListener('click', () => {
                this.#switch_slides(i)
            })
        }

        this.#prev_ctrl.addEventListener('click', () => {
            if (this.#current_slide_index === 0) {
                if (this.#config['loop']) {
                    this.#switch_slides(this.#slides.length - 1);
                }
            } else {
                this.#switch_slides(this.#current_slide_index - 1)
            }
        });

        this.#next_ctrl.addEventListener('click', () => {
            if (this.#current_slide_index === this.#slides.length - 1) {
                if (this.#config['loop']) {
                    this.#switch_slides(0);
                }
            } else {
                this.#switch_slides(this.#current_slide_index + 1)
            }
        });
    }

    #setup_controls() {
        if (this.#config['navs']) {
            this.#prev_ctrl.classList.add('enabled');
            this.#next_ctrl.classList.add('enabled');
        }
        if (this.#config['pagination']) {
            this.#pagination.classList.add('enabled')
        }
    }

    #setup_auto_rotation() {
        if (this.#config['auto']) {
            let delay = this.#config['delay'] === null ? 5000 : this.#config['delay']
            this.#interval_id = setInterval(() => {
                if (this.#current_slide_index === this.#slides.length - 1) {
                    this.#switch_slides(0)
                } else {
                    this.#switch_slides(this.#current_slide_index + 1);
                }
            }, delay)
        }
    }

    #setup_hover_behaviour() {
        if (this.#config['pause_on_hover']) {
            this.#slider.addEventListener('mouseover', () => {
                clearInterval(this.#interval_id);
            })
            this.#slider.addEventListener('mouseout', () => {
                this.#setup_auto_rotation();
            })
        }
    }

    #switch_slides(index) {
        this.#slides[this.#current_slide_index].classList.remove('active');
        this.#pagination_items[this.#current_slide_index].classList.remove('active');
        this.#captions[this.#current_slide_index].classList.remove('active');

        this.#current_slide_index = index;
        this.#slides[index].classList.add('active');
        this.#update_slider_counter();
        this.#update_pagination();
        this.#update_captions();
    }

    #update_slider_counter() {
        this.#slider_counter.innerHTML = `${this.#current_slide_index + 1} / ${this.#slides.length}`
    }

    #update_pagination() {
        this.#pagination_items[this.#current_slide_index].classList.add('active');
    }

    #update_captions() {
        this.#captions[this.#current_slide_index].classList.add('active');
    }
}
let slider = document.querySelector(".slider")
let pagination = slider.querySelector(".slider_pagination")

let sliderObj = new Slider({
    'slider': slider,
    'slider_counter' : slider.querySelector(".slider_counter"),
    'prev_ctrl' : slider.querySelector(".prev"),
    'next_ctrl' : slider.querySelector(".next"),
    'slides' : slider.querySelectorAll('.slider_image'),
    'captions' : slider.querySelectorAll(".slider_image_caption"),
    'pagination' : pagination,
    'pagination_items' : pagination.querySelectorAll(".slider_pagination_item"),});

