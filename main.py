from flask import Flask, redirect, render_template, request
from json import loads, dumps

app = Flask(__name__)


class Contacts:
    def __init__(self) -> None:
        file = open("contacts.json", "r")
        self.contacts = loads(file.read() + "}")
        file.close()

    def search(self, q:str):
        return [contact for contact in self.contacts if q in contact]

    def get_contacts_names(self):
        return [contact for contact in self.contacts]

    def write_to_contact_file(self, data:dict):
        file = open("contacts.json", "a")
        json_data = dumps(data)[1:-1]
        file.write("," + json_data)
        file.close()

@app.route("/")
def index():
    return redirect("/contact")

@app.route("/contact")
def contact():
    search = request.args.get('q', '')
    return render_template("index.html", contacts = (Contacts().search(search) 
                                                    if search else Contacts().get_contacts_names()))

@app.route("/contact/<name>")
def contactInfos(name):
    return render_template("contactInfo.html", name=name, contact=Contacts().contacts[name])

@app.get("/new_contact")
def add():
    return render_template("newContact.html")

@app.post("/new_contact")
def hum():
    Contacts().write_to_contact_file( {
            request.form['name']:{
                "number":request.form['number'],
                "email":request.form['email']
                } })
    return redirect("/")
