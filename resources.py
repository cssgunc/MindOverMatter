from __main__ import app
from flask import render_template


@app.route('/resources')
def resources():
    return render_template('resources.html')


class Resource:
    def __init__(self, link, title, description):
        self.link = link
        self.title = title
        self.description = description


# ResourcesList = []
# ResourcesList = {
#     [Resource("http://activeminds.web.unc.edu/", "Active Minds at Carolina",
#               "Active Minds at Carolina is a service and advocacy organization dedicated to raising awareness for and combating stigma against mental health issues on UNC’s campus and in the Chapel Hill community.")],
#     [Resource("https://heellife.unc.edu/organization/artheels", "Art Heels",
#               "ArtHeels is a service-based organization that is passionate about bringing art to the UNC campus and the surrounding community.")]
# }
