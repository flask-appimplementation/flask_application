from flask import Flask
from flask_script import Manager
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)
manager = Manager(app)
cors = CORS(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:root@localhost/flask_application"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '\xd10b\xc1\x181\x05\xd2\x97'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from views import *
from models import *


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))


# @app.route('/')
# def welcome():
#     return '<h2> WEL-COME</h2>'

# @app.route('/userlogin')
# def login():
#     u ="venkatesh";p ="12345"
#     l =User(u,p)
#     l.set_password(p)
#     db.session.add(l)
#     db.session.commit()
#     current_user = User.query.filter_by(name="venkatesh").first()
#     if current_user:
#         return '<h1>user name is already taken</h1>'
#     else:
#         return '<h2> USER CREATION IS SUCCESSFULL</h2>'



if __name__ == "__main__":
    app.run(debug=True)