from flask import Blueprint, redirect, render_template, jsonify, request, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

from App.models.user import db, User
from App.models.logIn import LogIn
logIn_views = Blueprint('logIn_views', __name__, template_folder='../templates')

@logIn_views.route('/logIn', methods=['GET'])
def logIn():
  form = LogIn()
  return render_template('login.html', form=form)


#user submits the login form
@logIn_views.route('/logIn', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']): # check credentials
        flash('Logged in successfully.') # send message to next page
        login_user(user) # login the user
        return render_template('index.html') # redirect to main page if login successful
  flash('Invalid credentials')
  return render_template('login.html', form=form)