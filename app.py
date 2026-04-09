from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask( )
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Interger,primary_key= True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    role= db.Column(db.String(200))
    
class Student(db.Model):
            id = db.Column(db.Interger,primary_key= True)
            cgpa = db.Column(db.String(200))
            resume_link = db.Column(db.String(200))
            user_id = db.Column(db.Interger,db.ForeignKey("user.id")) 
            
class Company(db.Model):
    
    id = db.Column(db.Interger,primary_key= True)
    age = db.Column(db.Interger(100))
    location = db.column(db.String(200))
    