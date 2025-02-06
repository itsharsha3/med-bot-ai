import tkinter as tk
from tkinter import scrolledtext, font
import requests

# Define colors and fonts
BG_COLOR = "#F0F0F0"
TEXT_COLOR = "#333333"
USER_BG = "#DCF8C6"
BOT_BG = "#FFFFFF"
FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 13 bold"

# Function to send a message
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    # Display user message
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    chat_window.config(state=tk.DISABLED)

    # Send message to Flask backend
    response = requests.post('http://127.0.0.1:5000/chat', json={'message': user_input})
    bot_response = response.json()['response']

    # Display bot response
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"Bot: {bot_response}\n\n", "bot")
    chat_window.config(state=tk.DISABLED)

    # Clear the input field
    entry.delete(0, tk.END)

    # Auto-scroll to the bottom
    chat_window.yview(tk.END)

# Create the main window
root = tk.Tk()
root.title("Medical Chatbot")
root.geometry("500x600")
root.resizable(False, False)

# Create a chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Configure tags for user and bot messages
chat_window.tag_configure("user", background=USER_BG, justify="right", lmargin1=100, lmargin2=10, rmargin=10)
chat_window.tag_configure("bot", background=BOT_BG, justify="left", lmargin1=10, lmargin2=100, rmargin=10)

# Create an input field
entry = tk.Entry(root, font=FONT, bg="white", fg=TEXT_COLOR)
entry.pack(padx=10, pady=10, fill=tk.X)

# Create a send button
send_button = tk.Button(root, text="Send", font=FONT_BOLD, bg="#4CAF50", fg="white", command=send_message)
send_button.pack(padx=10, pady=10, fill=tk.X)

# Bind Enter key to send message
root.bind('<Return>', lambda event: send_message())

# Start the Tkinter event loop
root.mainloop()