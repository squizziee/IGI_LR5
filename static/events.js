
function test() {
    alert("Kaboom");
}

function moveSidebar() {
    let burger = document.querySelector("#burger");
    burger.classList.toggle("active");

    let sidebar = document.querySelector("#sidebar");
    sidebar.classList.toggle("active")
}