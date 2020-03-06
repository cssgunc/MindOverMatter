from __main__ import app
from flask import render_template


@app.route('/resources')
def resources():
    return render_template('resources.html', ResourcesList=ResourcesList)


class Resource:
    def __init__(self, link, title, description):
        self.link = link
        self.title = title
        self.description = description


ResourcesList = []
ResourcesList = Resource("http://activeminds.web.unc.edu/", "Active Minds at Carolina",
                         "Active Minds at Carolina is a service and advocacy organization dedicated to raising awareness for and combating stigma against mental health issues on UNC’s campus and in the Chapel Hill community."), Resource("https://heellife.unc.edu/organization/artheels", "Art Heels", "ArtHeels is a service-based organization that is passionate about bringing art to the UNC campus and the surrounding community."), Resource("http://activeminds.web.unc.edu/", "Active Minds at Carolina",
                         "Active Minds at Carolina is a service and advocacy organization dedicated to raising awareness for and combating stigma against mental health issues on UNC’s campus and in the Chapel Hill community."), Resource("https://heellife.unc.edu/organization/artheels", "Art Heels", "ArtHeels is a service-based organization that is passionate about bringing art to the UNC campus and the surrounding community."), Resource("https://www.facebook.com/betanutheta/", "Beta Nu Theta", "Beta Nu Theta is UNC’s first black co-ed service fraternity, founded on the principles of activism, faith, service to others, and service to self.  Beta Nu Theta is for people who have a passion for people, mind-health, or just want to make new friends.")
