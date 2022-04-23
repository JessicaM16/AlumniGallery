from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required

from App.models.user import db, User

alumniListing_views = Blueprint('alumniListing_views', __name__, template_folder='../templates')

@alumniListing_views.route('/alumniListing')
def get_alumniListing():
    users=User.query.all()
    return render_template('alumniListing.html', users=users)
#graduation year, programme, faculty or department

@alumniListing_views.route('/searchUsers')
def users_search(search):
    return User.query.filter(
        User.name.like('%'+search+'%')
        | User.graduationyear.like('%'+search+'%')
        | User.programme.like('%'+search+'%')
        | User.faculty.like('%'+search+'%')
        | User.department.like('%'+search+'%')
    )
#User.name.like('%'+search+'%')

@alumniListing_views.route('/search')
def search():
    search= request.args.get('search')
    users=None
    if search:
        users=user_search(search)
    else:
        users=User.query.all()    
    #uh check sir recording 29:31 lect rec 24 for else
    return render_template('alumniListing.html', users=users)