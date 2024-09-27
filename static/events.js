
function test() {
    alert("Kaboom");
}

function moveSidebar() {
    let burger = document.querySelector("#burger");
    burger.classList.toggle("active");

    let sidebar = document.querySelector("#sidebar");
    sidebar.classList.toggle("active")
}

// document.addEventListener("load", function () {
//     let preloader = document.getElementById("preloader");
//     preloader.classList.add("ready");
// })