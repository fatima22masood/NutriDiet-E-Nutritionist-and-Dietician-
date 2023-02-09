from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('config.json', 'r') as c:
    params= json.load(c)["params"]
local_server= True

app = Flask(__name__)
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
class Contact(db.Model):
    '''sno, name, email, phone_num,msg, date'''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    phone_num = db.Column(db.String(12),  nullable=False)
    msg = db.Column(db.String(80),  nullable=False)
    date = db.Column(db.String, nullable= False)



@app.route("/")
def home():
    return render_template('index.html', params= params)    
@app.route("/home")
def home1():
    return render_template('index.html', params= params)    
@app.route("/about")
def About():
    return render_template('about.html', params= params)
@app.route("/contact", methods= ['GET', 'POST'])
def contact():
    if (request.method== 'POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone_num = request.form.get('phone_num')
        msg = request.form.get('msg')
        
        '''sno, name, email, phone_num,msg, date'''
        
        entry = Contact (name=name, phone_num= phone_num, msg= msg, email= email)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html', params= params)

@app.route("/services")
def services():
    return render_template('services.html', params= params)
@app.route("/login")
def login():
    return render_template('login.html', params= params)

app.run(debug= True)