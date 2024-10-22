let controls = document.querySelector('.page_style_picker')
let page_color_picker = controls.querySelector('#page_color')
let font_color_picker = controls.querySelector('#font_color')
let font_size_picker = controls.querySelector('#font_size')
let submit_btn = controls.querySelector('#submit')

let applied_area = document.querySelector('.content');

submit_btn.addEventListener('click', apply_styles);

function apply_styles() {
    applied_area.style.backgroundColor = page_color_picker.value
    applied_area.style.color = font_color_picker.value
    console.log(applied_area.style.fontSize)
    applied_area.style.fontSize = font_size_picker.value + "px"
}