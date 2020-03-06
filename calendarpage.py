from __main__ import app
from flask import render_template

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')