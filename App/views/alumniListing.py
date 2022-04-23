from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required

from App.models.user import db, User

alumniListing_views = Blueprint('alumniListing_views', __name__, template_folder='../templates')


def users_search(search):
    return User.query.filter(
        User.fullname.like('%'+search+'%')
        | User.graduationyear.like('%'+search+'%')
        | User.programme.like('%'+search+'%')
        | User.faculty.like('%'+search+'%')
        | User.department.like('%'+search+'%')
    )


@alumniListing_views.route('/alumniListing')
def search():
    search= request.args.get('search')
    users=None
    if search:
        users=users_search(search)
        return render_template('alumniListing.html', users=users, search=search)
    else:
        users=User.query.all() 
        return render_template('alumniListing.html', users=users, search=None)   
    
    