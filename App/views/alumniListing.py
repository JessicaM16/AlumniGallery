from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

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
