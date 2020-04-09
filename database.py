from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.link

@app.route("/addresource", methods=['GET', 'POST'])
def add_post():
    if request.method == "POST":
        post = Post(link=request.form["link"],title=request.form['title'],description=request.form['description'])
        db.session.add(post)
        db.session.commit()

    return render_template("addpost.html")

@app.route("/deletepost/<int:postid>")
def delete_post(postid):
    post = Post.query.get(postid)
    if post is not None:
        db.session.delete(post)
        db.session.commit()

    return redirect(url_for("hello_world"))


@app.route("/createdb")
def create_db():
    db.create_all()
    return "db created"

@app.route('/')
def hello_world():
    return render_template("index.html", posts=Post.query.all())

app.run(debug=True)

    