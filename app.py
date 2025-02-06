from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def generate_response(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["headache", "head ache"]):
        return "You might be experiencing a headache. Drink water, rest, and avoid bright lights. If it persists, consult a doctor."
    elif any(word in user_input for word in ["fever", "high temperature"]):
        return "You might have a fever. Take rest, stay hydrated, and monitor your temperature. If it persists or worsens, consult a doctor."
    elif any(word in user_input for word in ["cough", "cold"]):
        return "You might have a cold or cough. Drink warm fluids, rest, and avoid cold environments. If symptoms persist, consult a doctor."
    elif any(word in user_input for word in ["stomach", "stomach ache"]):
        return "You might have a stomach ache. Avoid heavy meals, drink plenty of water, and rest. If it persists, consult a doctor."
    else:
        return "I'm not sure about your condition. Please provide more details or consult a doctor."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({'response': response})

@app.route('/')
def home():
    return render_template('index.html')  # Serve from the templates folder

if __name__ == '__main__':
    app.run(debug=True)