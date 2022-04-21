from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

from App.models.user import db, User
from App.models.signUp import SignUp
signUp_views = Blueprint('signUp_views', __name__, template_folder='../templates')

@signUp_views.route('/signUp', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signUp.html', form=form) # pass form object to template



@signUp_views.route('/signUp', methods=['POST'])
def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(username=data['username'], email=data['email']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return render_template('index.html')# redirect to login page
  flash('Error invalid input!')
  return render_template('signUp.html', form=form)

 