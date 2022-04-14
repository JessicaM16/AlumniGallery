from flask import Blueprint, redirect, render_template, jsonify, request, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

from App.models.user import db, User

logIn_views = Blueprint('logIn_views', __name__, template_folder='../templates')

@logIn_views.route('/logIn', methods=['POST'])
def authenticate(uname, password):
  #search for the specified user
  user = User.query.filter_by(username=uname).first()
  #if user is found and password matches
  if user and user.check_password(password):
    return user