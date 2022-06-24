const StartingMin = 10;
let time = StartingMin * 60;

const Countdown = document.getElementById(''countdown');

setInterval(update_time, 1000)

function update_time{
    const min = Math.floor(time / 60);
    let sec = time % 60;
    Countdown.innerHTML = '${min}: ${sec}';
    time--;
}