from flask import Flask,render_template,flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired,Length
app = Flask(__name__)

app.config['SECRET_KEY'] = '1de2d95051ff6e819cdb7c62c92bdd5f'

class Form(FlaskForm):
    question = StringField('Question', validators=[DataRequired(),Length(min=10)])
    choice = SelectField('Choice', choices = ['Wikipedia','Google','Custom'])
    context = TextAreaField('Context', render_kw={"rows": 10, "cols": 11})
    submit = SubmitField('Submit')

@app.route("/", methods=['GET','POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        question = form.question.data
        context = form.context.data
        choice = form.choice.data
        return redirect(url_for('prediction',question = question, context=context, choice=choice))
    return render_template('home.html',form=form)
    
@app.route("/prediction")
def prediction():
    question = request.args['question']
    context = request.args['context']
    choice = request.args['choice']
    # answer = q_to_a(model, question, n=10)
    # print('Answer:', answer)
    answer = 'Hello'
    return render_template('prediction.html', answer = answer)

if __name__ == '__main__':
    app.run(debug=True)
    

