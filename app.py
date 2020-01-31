from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/help')
def get_help():
    return render_template('help.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')
