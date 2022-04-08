from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.models.user import db, User

signUp_views = Blueprint('signUp_views', __name__, template_folder='../templates')

@signUp_views.route('/signUp')
def get_signUp():
    userData=request.get_json()
    newUser= User(username=userData['username'], email=userData['email'])
    newUser.set_password(userData['password'])
    try:
        db.session.add(newUser)
        db.session.commit()
    except IntegrityError:
     db.session.rollback()
     return 'The username or email already exists'
    return 'User created'


