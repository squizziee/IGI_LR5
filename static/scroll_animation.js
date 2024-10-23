let animated = document.querySelectorAll('.scroll_animation');
let animatedImmovable = document.querySelectorAll('.scroll_animation_immovable');

// const observer = new IntersectionObserver(entries => {
//     entries.forEach(entry => {
//         let element = entry.target;
//         if (entry.isIntersecting) {
//             let rect = entry.boundingClientRect;
//             let middle = rect.top - window.screen.height / 2
//
//             let scale = middle / window.screen.height;
//             if (scale > 1) scale = 1
//             element.style.transform = `translateX(-${scale * 100}vw)`
//         }
//     });
// }, {
//     root: document,
//     threshold: 0.01  // Trigger when 50% of the block is visible
// });

//animated.forEach(el => observer.observe(el))

window.addEventListener('scroll', () => {
    requestAnimationFrame( () => {
        animated.forEach(element => {
            let rect = element.getBoundingClientRect();
            let middle = rect.top - window.screen.height / 2 + rect.height / 2

            let scale = middle / window.screen.height;
            if (scale > 1) scale = 1
            element.style.transform = `translateX(-${scale * 100}vw)`
        })
    })
    animatedImmovable.forEach(element => {
        let rect = element.getBoundingClientRect();
        let middle = rect.top - window.screen.height / 2 + rect.height / 2

        let scale =  1 - middle / window.screen.height;
        if (scale > 1) scale = 1
        element.style.transform = `scale(${scale})`
    })
})
