from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/testtemplate')
def testtemplate():
    return render_template('testtemplate.html')

@app.route('/testtemplate2')
def testtemplate2():
    return render_template('testtemplate2.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

import homepage
import test
import help

app.run(debug=True)
