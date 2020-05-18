from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from __main__ import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    other = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.link

# @app.route("/addresource", methods=['GET', 'POST'])
# def add_post():
#     if request.method == "POST":
#         post = Post(link=request.form["link"],title=request.form['title'],description=request.form['description'],email=request.form['email'],other=request.form['other'])
#         db.session.add(post)
#         db.session.commit()

#     return redirect(url_for("admin"))

@app.route("/editresource/<int:id>", methods=['POST'])
def edit_post(id):
    postid = Post.query.get(id)
    postid.link = request.form['linkedit']
    postid.title = request.form['titleedit']
    postid.description = request.form['textareaedit']
    postid.email = request.form['emailedit']
    postid.other = request.form['otheredit']
    db.session.commit()

    return redirect(url_for("admin"))

@app.route("/deletepost/<int:postid>")
def delete_post(postid):
    post = Post.query.get(postid)
    if post is not None:
        db.session.delete(post)
        db.session.commit()

    return redirect(url_for("admin"))

@app.route("/getinfo")
def get_info():
    return Post.query.all()

@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    if request.method == "POST":
        post = Post(link=request.form["link"],title=request.form['title'],description=request.form['description'],email=request.form['email'],other=request.form['other'])
        db.session.add(post)
        db.session.commit()

    return render_template('admin.html', info = get_info())

@app.route("/createdb")
def create_db():
    db.create_all()
    return "db created"

    