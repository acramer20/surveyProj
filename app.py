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
    
    return render_template('question.html', ques=ques)

@app.route('/answer', methods=["POST"])
def save_answer():
    responses.append(request.args('answer'))
    quid = 1

    return redirect('questions/{quid}')


    # example
#     ques = satisfaction_survey.questions

# ques1 = ques[0].question

# print(ques1)

# for que in ques:
#   print(que.question, que.choices)