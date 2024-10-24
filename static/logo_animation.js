const obj = document.querySelector('#logo')
obj.style.transformOrigin = '50% 50%'
const frames = [{
    transform: 'scale(1) rotate(0deg)',
    offset: 0
},{
    transform: 'scale(1.2) rotate(2.5deg)',
    offset: 0.125
},{
    transform: 'scale(1.2) rotate(-2.5deg)',
    offset: 0.25
},{
    transform: 'scale(1.2) rotate(2.5deg)',
    offset: 0.375
},{
    transform: 'scale(1.2) rotate(-2.5deg)',
    offset: 0.5
},{
    transform: 'scale(1) rotate(0deg)',
    offset: 1
},];

const config = {
    duration: 1000,
    easing: "ease-in-out",
    iterations: Infinity,
    direction: "normal",
};
const animation = obj.animate(frames, config);