import os
from flask import Flask, url_for, Markup, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/startOver")
def startOver():
    session.clear()
    return redirect(url_for("render_main"))
    
    
@app.route("/quiz1", methods=['get', 'post'])
def render_quiz1():
    return render_template('quiz1.html')
    
@app.route("/quiz2", methods=['get', 'post'])
def render_quiz2():
    if 'answer' in session:
        session.clear()
        return render_template('home.html')
    else:
        session['answer']=request.form['answer']
        return render_template('quiz2.html')
    
@app.route("/quiz3", methods=['get', 'post'])
def render_quiz3():
    if 'answer1' in session:
        session.clear()
        return render_template('home.html')
    else:
        session['answer1']=request.form['answer1']
        return render_template('quiz3.html')
    
@app.route("/quiz4", methods=['get', 'post'])
def render_quiz4():
    if 'answer2' in session:
        session.clear()
        return render_template('home.html')
    else:
        session['answer2']=request.form['answer2']
        return render_template('quiz4.html')
    
@app.route("/quiz5", methods=['get', 'post'])
def render_quiz5():
    if 'answer3' in session:
        session.clear()
        return render_template('home')
    else:
        session['answer3']=request.form['answer3']
        return render_template('quiz5.html')
    
@app.route("/quiz6", methods=['get', 'post'])
def render_quiz6():
    if 'answer4' in session:
        session.clear()
        return render_template('home.html')
    else:
        session['answer4']=request.form['answer4']
        return render_template('quiz6.html')
    
@app.route("/finished", methods=['get', 'post'])
def render_finished():
    if 'answer5' in session:
        session.clear()
        return render_template('home.html')
    else:
        session['answer5']=request.form['answer5']
        return redirect('/results')
        
@app.route("/results")
def render_results():
    count = results_count()
    return render_template('results.html', count = count)
    
def results_count():
    count = 0  
    if session['answer'] == '52':
        count = count + 1
    if session['answer1'] == '73':
        count = count + 1
    if session['answer2'] == '81':
        count = count + 1   
    if session['answer3'] == '80':
        count = count + 1  
    if session['answer4'] == '34':
        count = count + 1
    if session['answer5'] == '52':
        count = count + 1
    return count
    
if __name__=="__main__":
    app.run(debug=False)