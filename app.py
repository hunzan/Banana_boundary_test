from flask import Flask, render_template, request, redirect, url_for
from questions import questions, get_result

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        total_score = 0
        for i in range(len(questions)):
            answer = request.form.get(f"q{i}")
            if answer:
                total_score += questions[i]['options'][answer]['score']
        result = get_result(total_score)
        return render_template('result.html', result=result)
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
