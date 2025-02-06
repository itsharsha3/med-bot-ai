from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import os

app = Flask(__name__)

# Load the Medical AI model (example with Hugging Face Transformers)
# Replace this with a proper fine-tuned medical model if necessary
model = pipeline("question-answering", model="deepset/roberta-base-squad2")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"response": "Please provide a valid question."})
        
        # Example response generation
        context = (
            "This is a Medical AI Bot designed to answer your health-related questions. "
            "It is not a replacement for professional medical advice."
        )
        response = model(question=user_message, context=context)
        bot_reply = response.get("answer", "Sorry, I couldn't find an answer.")
        return jsonify({"response": bot_reply})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "An error occurred. Please try again later."})

if __name__ == "__main__":
    app.run(debug=True)
