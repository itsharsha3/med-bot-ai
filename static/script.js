document.getElementById("send-button").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    appendMessage(userInput, "user");

    const loading = document.createElement("div");
    loading.className = "message bot-message loading";
    loading.textContent = "Bot is typing...";
    appendMessage(loading, "bot");

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("chat-window").lastChild.remove();
            appendMessage(data.response, "bot");
        })
        .catch((error) => {
            document.getElementById("chat-window").lastChild.remove();
            appendMessage("Error connecting to the server.", "bot");
            console.error("Error:", error);
        });

    document.getElementById("user-input").value = "";
}

function appendMessage(text, sender) {
    const chatWindow = document.getElementById("chat-window");
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${sender}-message`;
    messageDiv.textContent = text;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
