from flask import Blueprint, redirect, render_template, jsonify, request, send_from_directory, flash
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

from App.models.user import db, User
#from App.models.logIn import LogIn
logIn_views = Blueprint('logIn_views', __name__, template_folder='../templates')

@logIn_views.route('/logIn')
def logIn():
  #form = LogIn()
  return render_template('login.html')

@logIn_views.route('/logIn', methods=['POST'])
def loginAction():
  username=request.form.get('username')
  password=request.form.get('password')
  remember=True if request.form.get('remember') else False
  
  userData=User.query.filter_by(username=username).first()

  

  if not userData or not userData.check_password(password):
    flash('Check Username and Password')
    return render_template('login.html')

  flash('Hello')
  return render_template('index.html')