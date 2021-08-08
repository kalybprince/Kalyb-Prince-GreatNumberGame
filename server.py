from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    print('Main index')
    # Create default session values
    if 'rand_num' not in session:
        session['rand_num'] = randint(0, 100)
    if 'guess' not in session:
        session['guess'] = 0
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    # Create default session value
    session['guess'] = int(request.form['guess'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
