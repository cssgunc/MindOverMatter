from __main__ import app
from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import db, Post
import re


@app.route('/resources/<int:resource>')
def resourceRoute(resource):
    return render_template('resourcesj.html', resource=Post.query.get(resource))

@app.route('/resources/')
def resources():
    return render_template('resources.html', ResourcesList=Post.query.all())

@app.route('/resources/search/<searchField>')
def resourceSearch(searchField):
    searchedList = list()
    for post in Post.query.all():
        currentPost = re.findall(searchField, post.title + post.description)
        print(currentPost)
        if currentPost != []:
            searchedList.append(post)
        print(searchedList)
    
    return render_template('resources.html', ResourcesList=searchedList)

    
