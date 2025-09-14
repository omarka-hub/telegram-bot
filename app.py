from flask import Flask, render_template, request
from script import quiz_bot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Flask will look in templates/

@app.route('/submit', methods=['POST'])
def submit():
    questions = request.form.get('questions')
    status = quiz_bot(questions)
    return status

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

