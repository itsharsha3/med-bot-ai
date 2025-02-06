from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a simple model as a placeholder
model = pipeline("question-answering", model="deepset/roberta-base-squad2")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Please provide a valid question."})

    context = "This is a Medical AI Bot designed to answer your health-related questions. " \
              "It is not a replacement for professional medical advice."
    try:
        response = model(question=user_message, context=context)
        bot_reply = response.get("answer", "I'm sorry, I couldn't find an answer.")
    except Exception as e:
        bot_reply = "An error occurred in processing your request."

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
