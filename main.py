from flask import Flask, redirect, render_template, request
import json

app = Flask(__name__)


class Contacts:
    def __init__(self) -> None:
        file = open("contacts.json", "r")
        self.contacts = json.loads(file.read())
        file.close()

    def search(self, q:str):
        return [contact['name'] for contact in self.contacts if q in contact['name']]

    def getContactsNames(self):
        return [contact['name'] for contact in self.contacts]

bibib = Contacts()


@app.route("/")
def index():
    return redirect("/contact")

@app.route("/contact")
def contact():
    search = request.args.get('q', '')
    if search:
        return render_template("index.html", numbers=bibib.search(search))
    else:
        return render_template("index.html", numbers=bibib.getContactsNames())

# @app.route("/contact/<name>")
# def contactInfos():
    
