from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

#from App.models.users import db, User

signUp_views = Blueprint('signUp_views', __name__, template_folder='../templates')

@signUp_views.route('/signUp')
def get_signUp():
    userData=request.get_json()
    newUser= User(username=userDate['username'], email=userDate['email'])
    newUser.set_password(userData['password'])
    try:
        db.session.add(newUser)
        db.session.commit()
    except IntegrityError:
     db.session.rollback()
     return 'The username or email already exists'
    return 'User created'


'''
@app.route('/signup', methods=['POST'])
def signup():
  userdata = request.get_json() # get json data
  newuser = User(username=userdata['username'], email=userdata['email']) # create user object
  newuser.set_password(userdata['password']) # set password
  try:
    db.session.add(newuser)
    db.session.commit() # save user
  except IntegrityError: # attempted to insert a duplicate user
    db.session.rollback()
    return 'username or email already exists' # error message
  return 'user created' # success
'''