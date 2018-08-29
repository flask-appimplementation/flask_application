from app import db
# from werkzeug.security import generate_password_hash
# from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, \
     check_password_hash
import re



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
#     password = db.Column(db.String(120))
    
#     def __init__(self, name, password):
#         self.name = name
#         self.password = self.set_password(password)

#     def set_password(self, password):
#         return generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.pw_hash, password)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    renterpassword = db.Column(db.String(120),nullable=False)

    def __init__(self, username, password,email,renterpassword):
        self.username = username
        self.email = email
        self.renterpassword =renterpassword
        self.password = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, passwordcheck):
        return check_password_hash(self.password, passwordcheck)

    def password_check(self,password,renterpassword):
        print(password,renterpassword)
        if password==renterpassword:
            return True

   
