from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_fontawesome import FontAwesome
app = Flask(__name__)
fa = FontAwesome(app)

from flask import render_template

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

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
def home():
    return render_template('homepage.html')

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     content = db.Column(db.String, unique=True, nullable=False)

#     def __repr__(self):
#         return '<Post %r>' % self.name

# @app.route("/adminpage", methods=['GET', 'POST'])
# def add_post():
#     if request.method == "POST":
#         post = Post(name=request.form["name"], content=request.form['content'])
#         db.session.add(post)
#         db.session.commit()

#     return render_template("adminpage.html")

import calendarpage
import homepage
import test
import help
import database
import resources
import aboutus
import adminpage

app.run(debug=True)



