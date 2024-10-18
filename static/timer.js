let timer = document.querySelector(".timer");
let time = timer.querySelector(".time");
let reset_btn = timer.querySelector(".reset_timer");

if (!localStorage.getItem('timer_end')) {
    let timer_end = Date.now() + 60000 * 60;
    localStorage.setItem('timer_end', timer_end.toString());
}

let timer_end = localStorage.getItem('timer_end')
let date = new Date(Number(timer_end))

let curr_interval_id = start_timer(date);

reset_btn.addEventListener('click', () => {
    let new_timer_end = Date.now() + 60000 * 60;
    localStorage.setItem('timer_end', new_timer_end.toString());
    clearInterval(curr_interval_id);
    curr_interval_id = start_timer(new Date(Number(new_timer_end)));
})

function start_timer(timer_end) {
    return setInterval(() => {
        let current_date = new Date()

        if (timer_end - current_date < 0) {
            update_time(0, 0, 0, 0);
            clearInterval(curr_interval_id);
        } else {
            let diff = (Math.abs(timer_end - current_date));
            let days = Math.floor(diff/(1000*60*60*24));
            let hours = Math.floor((diff%(1000*60*60*24))/(1000*60*60));
            let minutes = Math.floor((diff%(1000*60*60))/(1000*60));
            let seconds = Math.floor((diff%(1000*60))/1000);
            //console.log(`${days}:${hours}:${minutes}:${seconds}`)
            update_time(days, hours, minutes, seconds);
        }
    }, 1000);
}

function update_time(days, hours, minutes, seconds) {
    let text_days = num_len(days) === 2 ? days : '0' + days
    let text_hours = num_len(hours) === 2 ? hours : '0' + hours
    let text_minutes = num_len(minutes) === 2 ? minutes : '0' + minutes
    let text_seconds = num_len(seconds) === 2 ? seconds : '0' + seconds
    time.innerHTML = `${text_days}:${text_hours}:${text_minutes}:${text_seconds}`;
}

function num_len(num) {
    if (num === 0) return 1;
    return Math.floor(Math.log10(num) + 1);
}