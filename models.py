from app import db,bcrypt
# from werkzeug.security import generate_password_hash
# from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, \
     check_password_hash



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(120))
    
    def __init__(self, name, password):
        self.name = name
        self.password = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)