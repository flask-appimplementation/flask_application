from flask import Flask
from flask_script import Manager
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
# from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)
manager = Manager(app)
# bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:root@localhost/flask_application"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '\xd10b\xc1\x181\x05\xd2\x97'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
from views import *
from models import  *

if __name__ == "__main__":
    app.run(debug=True)