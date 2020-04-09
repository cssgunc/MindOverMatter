from __main__ import app
from flask import render_template

@app.route('/database')
def database():
    return render_template('database.html')

    