from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

from App.models.user import db, User
from App.controllers import create_user
#from App.models.signUp import SignUp
signUp_views = Blueprint('signUp_views', __name__, template_folder='../templates')

@signUp_views.route('/signUp')
def signup():
  #form = SignUp() # create form object
  return render_template('signUp.html') # pass form object to template



@signUp_views.route('/signUp', methods=['POST'])
def signUpAction():
    
    username=request.form.get('username')
    fullname=request.form.get('fullname')
    password=request.form.get('password')
    email=request.form.get('email')
    faculty=request.form.get('faculty')
    graduationyear=request.form.get('graduationyear')
    programme=request.form.get('programme')
    department=request.form.get('department')
    linkedIn=request.form.get('linkedIn')
    facebook=request.form.get('facebook')
    instagram=request.form.get('instagram')

    userData= User.query.filter_by(username=username).first()


    if userData:
      flash('Username already exists')
      return render_template('signUp.html')

    #newUser=create_user(username, fullname,password, email,faculty,graduationyear,programme,department, linkedIn, facebook,instagram)
    newuser = User(username=username, fullname=fullname,password=password, email=email,faculty=faculty, graduationyear=graduationyear,programme=programme,department=department, linkedIn=linkedIn, facebook=facebook,instagram=instagram)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError:
     db.session.rollback()
     flash('The username or email already exists')
     return render_template('signUp.html')
    # flash(newuser.username)
    
    flash('SignUp Successful, ')
    flash(username)
    return render_template('login.html')


# @signUp_views.route('/signUp', methods=['POST'])
# def signUp():
#     userData=request.form
#     newUser= User(username=userData['username'], email=userData['email'], graduationyear=userData['graduationyear'], programme=userData['programme'], faculty=userData['faculty'], department=userData['department'])
#     newUser.set_password(userData['password'])
    
#     try:
#         db.session.add(newUser)
#         db.session.commit()
#     except IntegrityError:
#      db.session.rollback()
#      return 'The username or email already exists'
#     #return 'User created'
#     return render_template('index.html')