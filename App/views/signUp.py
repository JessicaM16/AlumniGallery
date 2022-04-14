from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

from App.models.user import db, User

signUp_views = Blueprint('signUp_views', __name__, template_folder='../templates')

@signUp_views.route('/signUp', methods=['POST'])
def signUp():
    userData=request.form
    newUser= User(username=userData['username'], email=userData['email'], graduationyear=userData['graduationyear'], programme=userData['programme'], faculty=userData['faculty'], department=userData['department'])
    newUser.set_password(userData['password'])
    
    try:
        db.session.add(newUser)
        db.session.commit()
    except IntegrityError:
     db.session.rollback()
     return 'The username or email already exists'
    #return 'User created'
    #return render_template('index.html')


@signUp_views.route('/signUp', methods=['GET'])
def signUpPage():
    return render_template('signUp.html')