from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory quiz questions
questions = [
    {"id": 1, "question": "What is Python?", 
     "options": ["Snake", "Programming Language", "Car"], "answer": "Programming Language"},
    {"id": 2, "question": "Which framework is this?", 
     "options": ["Django", "Flask", "FastAPI"], "answer": "Flask"}
]

# Home route
@app.route("/")
def home():
    return "Quiz Backend is running with Flask 🚀"

# Get quiz questions
@app.route("/quiz", methods=["GET"])
def get_quiz():
    return jsonify(questions)

# Submit answers
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json   # Expect {"user": "Alice", "answers": {1: "Programming Language", 2: "Flask"}}
    user = data.get("user")
    answers = data.get("answers", {})

    # Score calculation
    score = 0
    for q in questions:
        qid = q["id"]
        if str(qid) in answers and answers[str(qid)] == q["answer"]:
            score += 1

    return jsonify({"user": user, "score": score, "total": len(questions)})

if __name__ == "__main__":
    app.run(debug=True)
