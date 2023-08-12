const toggleButton = document.getElementById('expand-mimicry-bar-toggle');
const wrapper = document.getElementById('mimicry-wrapper');

toggleButton.addEventListener('click', () => {
    if (wrapper.classList.contains('collapsed')) {
        wrapper.classList.remove('collapsed');
        wrapper.classList.add('expanded');
        toggleButton.innerText = 'Collapse';
    } else {
        wrapper.classList.remove('expanded');
        wrapper.classList.add('collapsed');
        toggleButton.innerText = 'Expand';
    }
});

let timerDisplay = document.getElementById('mimicry-simulation-timer').textContent;
if (/^\d+:\d{2}:\d{2}$/.test(timerDisplay)) {
    let [hours, minutes, seconds] = timerDisplay.split(":").map(Number);

    // Convert initial time to milliseconds
    let initialTime = hours * 3600000 + minutes * 60000 + seconds * 1000;
    let startTime = Date.now() - initialTime;

    let timerInterval;

    function startTimer() {
        timerInterval = setInterval(() => {
            let timeElapsed = Date.now() - startTime;
            let hrs = Math.floor(timeElapsed / 3600000);
            timeElapsed %= 3600000;
            let mins = Math.floor(timeElapsed / 60000);
            timeElapsed %= 60000;
            let secs = Math.floor(timeElapsed / 1000);

            let formattedTime = `${strPad(hrs, 2)}:${strPad(mins, 2)}:${strPad(secs, 2)}`;
            document.getElementById('timer').textContent = formattedTime;
        }, 1000);
    }

    function strPad(value, length) {
        return value.toString().padStart(length, '0');
    }

    startTimer();
}