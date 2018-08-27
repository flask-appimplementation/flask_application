from app import app,db
from models import *

@app.route("/home")
def intro():
    return '<p>intro</p>'
@app.route('/')
def home():
    return '<h2> WEL-COME</h2>'


@app.route('/userlogin')
def login():
    u ="venkatesh";p ="12345"
    l =User(u,p)
    l.set_password(p)
    db.session.add(l)
    db.session.commit()
    current_user = User.query.filter_by(name="venkatesh").first()
    if current_user:
        return '<h1>user name is already taken</h1>'
    else:
        return '<h2> USER CREATION IS SUCCESSFULL</h2>'