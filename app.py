from crypt import methods
from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from surveys import Question, Survey, surveys, satisfaction_survey

"""Must define RESPONSES_KEY for sessions"""
RESPONSES_KEY = 'responses'

app = Flask(__name__)
app.config['SECRET_KEY'] = "dont-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route('/')
def title_page():
    """Home page to start survey"""
    return render_template('title_page.html', survey=surveys)


@app.route('/start', methods=['POST'])
def question_0():
    """using sessions to create a list to be passed back and forth bewteen browser and server
    reditecting to the first question"""
    session[RESPONSES_KEY] = []
    return redirect('/questions/0')

@app.route('/questions/<int:quid>')
def show_question(quid):
    """dynamically rendering the question based on the quid that we get from the /answer route"""
    responses = session.get(RESPONSES_KEY)

    if (len(responses) != quid):
        # Trying to access questions out of order.
        flash(f"Invalid question id: {quid}.")
        return redirect(f"/questions/{len(responses)}")

    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/complete")
    
    ques=satisfaction_survey.questions[quid]
    
    
    return render_template('question.html', ques=ques)

@app.route('/answer', methods=["POST"])
def save_answer():
    """saving answer to list and redirecting to next question by comparing to how many answers are in the list"""
    
    choice = request.form['answer']
    responses = session[RESPONSES_KEY]
    responses.append(f"{choice}")
    session[RESPONSES_KEY] = responses

    # print("*******************")
    # print(session.get(RESPONSES_KEY))
    # print("**************")

    quid = len(responses)

    if len(responses) == 4:
        return redirect ('/complete')
    else:
        return redirect(f'questions/{quid}')\

@app.route('/complete')
def complete_survey():
    """Just letting them know they are done with survey when the list length is equal to the num of questions"""
    return render_template('complete.html')


    


    # example
#     ques = satisfaction_survey.questions

# ques1 = ques[0].question

# print(ques1)

# for que in ques:
#   print(que.question, que.choices)