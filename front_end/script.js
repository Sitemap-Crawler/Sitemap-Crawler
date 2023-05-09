const form = document.getElementById('submit-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async event => {
    event.preventDefault();

    const urlInput = document.getElementById('url-input');
    const url = urlInput.value;

    const response = await fetch('http://localhost:8000/urlCheck', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
    });

    const data = await response.json();

    if (response.ok) {
        resultDiv.textContent = `Success: ${data.message}`;
    } else {
        resultDiv.textContent = `Error: ${data.error}`;
    }
});
