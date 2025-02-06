document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

document.getElementById('clear-button').addEventListener('click', clearChat);

function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    if (userInput === "") return;

    // Display user message
    appendMessage(userInput, 'user');

    // Send message to Flask backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        appendMessage(data.response, 'bot');
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Clear the input field
    document.getElementById('user-input').value = '';
}

function appendMessage(message, sender) {
    const chatWindow = document.getElementById('chat-window');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `${sender}-message`);
    messageElement.textContent = message;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function clearChat() {
    const chatWindow = document.getElementById('chat-window');
    chatWindow.innerHTML = ''; // Clear all messages
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    if (userInput === "") return;

    // Display user message
    appendMessage(userInput, 'user');

    // Show typing indicator
    const typingIndicator = document.createElement('div');
    typingIndicator.classList.add('typing-indicator');
    typingIndicator.innerHTML = '<span></span><span></span><span></span>';
    appendMessage(typingIndicator, 'bot');

    // Send message to Flask backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Remove typing indicator
        const chatWindow = document.getElementById('chat-window');
        chatWindow.removeChild(chatWindow.lastChild);

        // Display bot response
        appendMessage(data.response, 'bot');
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Clear the input field
    document.getElementById('user-input').value = '';
}
document.getElementById('emoji-button').addEventListener('click', function () {
    const userInput = document.getElementById('user-input');
    userInput.value += '😀'; // Add an emoji to the input field
});