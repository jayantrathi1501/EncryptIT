function toggleDarkMode() {
    const body = document.body;
    const darkModeSwitch = document.getElementById('dark-mode');
    const label = document.querySelector('.dark-mode-switch label');

    body.classList.toggle('dark-mode');
    darkModeSwitch.checked = !darkModeSwitch.checked;
    if (body.classList.contains('dark-mode')) {
        label.textContent = 'Light Mode';
    } else {
        label.textContent = 'Dark Mode';
    }
}

function copyText() {
    const outputElement = document.querySelector('.output');
    const outputText = outputElement.textContent.trim();

    if (outputText) {
        const tempElement = document.createElement('textarea');
        tempElement.value = outputText;

        document.body.appendChild(tempElement);
        tempElement.select();
        document.execCommand('copy');
        document.body.removeChild(tempElement);
    } else {
        alert('Nothing to copy. Please encrypt or decrypt text first.');
    }
}
