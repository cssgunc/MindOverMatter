from __main__ import app
from flask import render_template





class Resource:
    def __init__(self, link, title, description):
        self.link = link
        self.title = title
        self.description = description

chat_list = [
    Resource("https://suicidepreventionlifeline.org/chat/", "Suicide Chatline", "Get in touch with a counselor who will listen to you, understand how your problem is affecting you, provide support and share resources that may be helpful."),
    Resource("https://www.nami.org/", "National Alliance on Mental Health Chatline", "Connect with a trained crisis counselor to receive free, 24/7 crisis support via text message.")
]
call_list = [
    Resource("https://www.townofchapelhill.org/town-hall/departments-services/police/contact-us", "Chapel Hill Police", "To report a previous or current crime, call 911"),
    Resource("tel:919-966-3658", "CAPS 24/7 Hotline", "Contact trained mental health professionals for any mental-health related crises"),
    Resource("https://suicidepreventionlifeline.org/", "Suicide Hotline", "Provies free and confidential emotional support to people in suicidal crisis or emotional distress 24 hours a day, 7 days a week, across the U.S."),
    Resource("https://www.nami.org/", "National Alliance on Mental Health Hotline", "Nationwide peer-support service providing information, resourse referrals, and support to people living with mental health conditions, their family members and caregivers, mental health providers and the public.")
]

website_list = [
    Resource("https://www.nami.org/", "National Alliance on Mental Health", "Advocacy, education, support, and public awareness for individuals and families affected by mental illness."),
    Resource("https://healgrief.org/grief-support-resources/", "HelpGrief", "Support network and resources for anyone going through grief or loss"),
    Resource("https://mentalhealth.gov", "MentalHealth.GOV", "National mental health information and education")
]

@app.route('/help/')
def get_help():
    return render_template('GitHelpNow1.html', chat_list=chat_list, call_list = call_list, website_list = website_list)