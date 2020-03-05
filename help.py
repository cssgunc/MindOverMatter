from __main__ import app
from flask import render_template
from flask import Flask


class Resource:
    def __init__(self, link, title, description, category):
        self.link = link
        self.title = title
        self.description = description
        self.category = category

help_list = {
    Resource("link", "title", "description", "call"), 
    Resource("https://suicidepreventionlifeline.org/chat/", "Suicide Chatline", "Get in touch with a counselor who will listen to you, understand how your problem is affecting you, provide support and share resources that may be helpful.", "chat_resource_one"),
    Resource("https://www.nami.org/", "National Alliance on Mental Health Chatline", "Connect with a trained crisis counselor to receive free, 24/7 crisis support via text message.", "chat_resource_two"),
    Resource("link", "title", "description", "website")
}

@app.route('/help')
def get_help():
    return render_template('GitHelpNow1.html', help_list=help_list)