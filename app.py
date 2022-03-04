from crypt import methods
from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from surveys import Question, Survey, surveys, satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "dont-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def title_page():
    
    return render_template('title_page.html', survey=surveys)


@app.route('/start', methods=['POST'])
def question_0():
    return redirect('/questions/0')

@app.route('/questions/<int:quid>')
def show_question(quid):

    ques=satisfaction_survey.questions[quid]

    if (len(responses) != quid):
        # Trying to access questions out of order.
        flash(f"Invalid question id: {quid}.")
        return redirect(f"/questions/{len(responses)}")
    
    
    return render_template('question.html', ques=ques)

@app.route('/answer', methods=["POST"])
def save_answer():
    """saving answer to list and redirecting to next question"""
    responses.append(request.form['answer'])
    quid = len(responses)

    if len(responses) == 4:
        return redirect ('/complete')
    else:
        return redirect(f'questions/{quid}')\

@app.route('/complete')
def complete_survey():
    """Just letting them know they are done with survey"""
    return render_template('complete.html')


    


    # example
#     ques = satisfaction_survey.questions

# ques1 = ques[0].question

# print(ques1)

# for que in ques:
#   print(que.question, que.choices)