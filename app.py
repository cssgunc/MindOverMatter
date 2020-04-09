from flask import Flask
from flask_fontawesome import FontAwesome
app = Flask(__name__)
fa = FontAwesome(app)

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

import calendarpage
import homepage
import test
import help
import database
import resources

app.run(debug=True)
