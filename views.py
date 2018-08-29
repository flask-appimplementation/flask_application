from app import app, db
from flask import jsonify, request, Response
from models import *
from flask_cors import CORS, cross_origin

def isValidEmail(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
        return False

@app.route("/home")
def intro():
    return '<p>intro</p>'


@app.route('/')
def home():
    return '<h2> WEL-COME</h2>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(
        "request:{0} --------request method:{1}".format(request, request.method))
    print(request.json)
    if request.method == 'POST':
        try:
            print("-"*20)
            current_user = Users.query.filter_by(email=request.json['email']).first()
            if current_user:
                password_verify = current_user.check_password(request.json['password'])
                print("password:genreated",password_verify)
                print("database_password:",current_user.password)
                if password_verify:
                    return Response("user is successfully logged in",status=200)
                else:    
                    return Response("password is incorrect",status=400)
            return Response("user is not found in database",status=400)
        except:
            raise


@app.route('/signup', methods=['POST'])
def signup():
    print("request:{0} --------request method:{1}".format(request, request.method))
    print(request.json)
    try:
        print("-"*20)
        print(request)
        current_user = Users.query.filter_by(email=request.json['email']).first()
        print(Users.query.filter_by(email=request.json['email']).first())
        if None == Users.query.filter_by(email=request.json['email']).first():
            print("user does not exists")
            if isValidEmail(request.json['email']):
                u = Users(request.json['username'], request.json['password'],request.json['email'],request.json['renterpassword'])
                db.session.add(u)
                db.session.commit()
            else:
                return Response("invalid email address",status=409) 
            return Response ("user is created successfully",status=200)
        elif Users.query.filter_by(email=request.json['email']).first():
            return Response("user is already exist",status=409)

    except Exception as e:
        print("-----------------------------------------------------------------")
        print(e)
        return jsonify({"message":"email is already exists"})


@app.route("/forgotpassword",methods=['POST'])
def forgotpassword():
    try:
        print("-"*20)
        print(request.json['renterpassword'],request.json['password'])
        if request.json['renterpassword'] == request.json['password']:
            print("yyyyyyesssssssssssss")
        current_user = Users.query.filter_by(email=request.json['email']).first()
        if None == Users.query.filter_by(email=request.json['email']).first():
            return Response("user does not exist",status=409)
        elif Users.query.filter_by(email=request.json['email']).first():
            if current_user.password_check(request.json['password'],request.json['renterpassword']):
                current_user.password=current_user.set_password(request.json['password'])
                current_user.renterpassword= request.json['renterpassword']
                db.session.add(current_user)
                db.session.commit()
                return Response("password is updated",status=200)
            else:
                return Response("Entered passwords should be match",status=409)
            return Response ("user is created successfully",status=200)
        elif Users.query.filter_by(email=request.json['email']).first():
            return Response("user is already exist",status=409)
    except:
        raise