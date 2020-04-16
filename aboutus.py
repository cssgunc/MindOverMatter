from __main__ import app
from flask import render_template

@app.route('/aboutus/')
def aboutus():
    return render_template('aboutus.html')