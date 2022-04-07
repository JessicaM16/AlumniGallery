from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.models.jobs import db, Job

jobBoard_views = Blueprint('jobBoard_views', __name__, template_folder='../templates')

@jobBoard_views.route('/jobBoard', methods=['GET'])
def get_jobBoard():
    board=Job.query.all()
    
    return render_template('jobBoard.html', board=board)

