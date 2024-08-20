document.addEventListener('DOMContentLoaded', (event) => {
    function appendMessage(sender, message) {
        const chatLog = document.getElementById('chat-log');
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);

        if (sender === 'bot') {
            // Replace **bold text** with <b>bold text</b>
            const formattedMessage = message.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');
            messageDiv.innerHTML = formattedMessage; // Allow HTML for bot messages
        } else {
            messageDiv.textContent = message; // Use textContent for user messages to prevent HTML injection
        }

        const messageContainer = document.createElement('div');
        messageContainer.classList.add('message-container');
        messageContainer.appendChild(messageDiv);

        chatLog.appendChild(messageContainer);
        chatLog.scrollTop = chatLog.scrollHeight;
    }

    function showThinkingAnimation() {
        document.getElementById('loading').classList.add('show');
    }

    function hideThinkingAnimation() {
        document.getElementById('loading').classList.remove('show');
    }

    function showTypingIndicator() {
        document.getElementById('typing-indicator').classList.add('show');
    }

    function hideTypingIndicator() {
        document.getElementById('typing-indicator').classList.remove('show');
    }

    function sendMessage() {
        const chatInput = document.getElementById('chat-input');
        const message = chatInput.value.trim();
        if (message !== '') {
            appendMessage('user', message);
            chatInput.value = '';

            showThinkingAnimation();
            showTypingIndicator();

            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                appendMessage('bot', data.reply);
                hideThinkingAnimation();
                hideTypingIndicator();
            })
            .catch(error => {
                console.error('Error:', error);
                hideThinkingAnimation();
                hideTypingIndicator();
            });
        }
    }

    function clearChat() {
        const chatLog = document.getElementById('chat-log');
        chatLog.innerHTML = '';
    }

    function downloadChat() {
        const chatLog = document.getElementById('chat-log').innerText;
        const blob = new Blob([chatLog], { type: 'text/plain' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'chat_log.txt';
        a.click();
    }

    document.getElementById('send-button').addEventListener('click', sendMessage);
    document.getElementById('clear-chat-button').addEventListener('click', clearChat);
    document.getElementById('download-chat-button').addEventListener('click', downloadChat);

    document.getElementById('theme-toggle').addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
    });

    document.getElementById('chat-input').addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    });
});
