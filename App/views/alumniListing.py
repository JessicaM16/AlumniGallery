from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required

from App.models.user import db, User

alumniListing_views = Blueprint('alumniListing_views', __name__, template_folder='../templates')

@alumniListing_views.route('/alumniListing')
def get_alumniListing():
    lists=(
        ("Jane Doe", "jane.doe@gmail.com"),
        ("John Doe", "john.doe@gmail.com"),
        ("Alice Character", "alice.character@gmail.com"),
        ("Bob Character", "bob.character@gmail.com")
    )
    return render_template('alumniListing.html', lists=lists)
#graduation year, programme, faculty or department

def users_search(search):
    return User.query.filter(
        User.name.like('%'+search+'%')
        | User.graduationyear.like('%'+search+'%')
        | User.programme.like('%'+search+'%')
        | User.faculty.like('%'+search+'%')
        | User.department.like('%'+search+'%')
    )
#User.name.like('%'+search+'%')

@alumniListing_views.route('/')
def search():
    search= request.args.get('search')
    users=None
    if search:
        users=user_search(search)
    else:
        users=User.query.all()    
    #uh check sir recording 29:31 lect rec 24 for else
    return render_template('alumniListing.html', users=users)