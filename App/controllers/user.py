from App.models import User
from App.database import db


def get_all_users():
    return User.query.all()

def create_user(username, password, email,faculty,graduationyear,programme,department, linkedIn, facebook, instagram):
    newuser = User(username=username, password=password, email=email,faculty=faculty, graduationyear=graduationyear,programme=programme,department=department, linkedIn=linkedIn, facebook=facebook,instagram=instagram)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users