from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Example bot responses
greetings = ["Hello! How can I assist you today?", "Hi there! How are you doing today?", "Hey! What brings you here today?"]
health_tips = [
    "Remember to drink plenty of water.",
    "Try to get at least 7-8 hours of sleep.",
    "Make sure to take short breaks if you're working long hours.",
    "If you're feeling unwell, it's best to consult a healthcare professional.",
    "Don't forget to eat balanced meals.",
]
critical_advice = "This issue might be critical. Please seek medical help immediately."

def generate_response(user_message):
    user_message = user_message.lower()
    if any(greet in user_message for greet in ["hello", "hi", "hey"]):
        return random.choice(greetings)
    if any(word in user_message for word in ["headache", "fever", "pain", "sick"]):
        return critical_advice
    if any(word in user_message for word in ["water", "sleep", "health", "tired"]):
        return random.choice(health_tips)
    return random.choice(["That's interesting!", "Could you tell me more?", "I'm here to listen."])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Please say something!"})
    bot_reply = generate_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
