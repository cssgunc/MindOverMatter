from __main__ import app
from flask import render_template
from flask import Flask

@app.route('/help')
def get_help():
    return render_template('GitHelpNow1.html')