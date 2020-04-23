from __main__ import app
from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# @app.route("/getresource", methods=["GET"])
# def getresource():
#     resource = db.request.form.get('addresource')
#     return jsonify(resource)


@app.route('/resources/<int:resource>')
def resourceRoute(resource):
    resource=ResourcesList[resource]
    return render_template('resourcesj.html', resource=resource)

@app.route('/resources')
def resources():
    return render_template('resources.html', ResourcesList=ResourcesList)


class Resource:
    def __init__(self, link, title, description, other):
        self.link = link
        self.title = title
        self.description = description
        self.other = other


ResourcesList = [Resource("http://activeminds.web.unc.edu/", "Active Minds at Carolina","Active Minds at Carolina is a service and advocacy organization dedicated to raising awareness for and combating stigma against mental health issues on UNC’s campus and in the Chapel Hill community.", "They meet twice a month on Mondays from 6:30-7:30 in Howell 115 or Dey 305. Active Minds begins meetings by talking about how everyone is doing, followed by watching a Ted Talk, listening to a guest speaker, or discussing an issue at UNC.  They have three committees that plan projects and events on campus: programming, outreach, and publicity. Form to be added to Listserv available here: https://docs.google.com/forms/d/e/1FAIpQLSfhl6wfcGZh86y7vIipV_Ym2izETWK36vgbMDcKiRucAgfIng/viewform"), Resource("https://heellife.unc.edu/organization/artheels", "Art Heels", "ArtHeels is a service-based organization that is passionate about bringing art to the UNC campus and the surrounding community.", "Other"), Resource("http://activeminds.web.unc.edu/", "Active Minds at Carolina","Active Minds at Carolina is a service and advocacy organization dedicated to raising awareness for and combating stigma against mental health issues on UNC’s campus and in the Chapel Hill community.", "Other"), Resource("https://heellife.unc.edu/organization/artheels", "Art Heels", "ArtHeels is a service-based organization that is passionate about bringing art to the UNC campus and the surrounding community.", "Other"), Resource("https://www.facebook.com/betanutheta/", "Beta Nu Theta", "Beta Nu Theta is UNC’s first black co-ed service fraternity, founded on the principles of activism, faith, service to others, and service to self.  Beta Nu Theta is for people who have a passion for people, mind-health, or just want to make new friends.", "Other")]


