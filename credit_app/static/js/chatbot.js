document.getElementById('chat-send').addEventListener('click', function() {
    const message = document.getElementById('chat-input').value;
    if (message.trim()) {
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
        document.getElementById('chat-input').value = '';

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `message=${message}`
        })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    }
});
