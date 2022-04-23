from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    #name=db.Column(db.String, nullable=False)
    email=db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    graduationyear=db.Column(db.Integer, nullable=False)
    programme=db.Column(db.String(120),nullable=False)
    faculty=db.Column(db.String(120),nullable=False)
    department=db.Column(db.String(120),nullable=False)
    
    linkedIn=db.Column(db.String(120), nullable=False)
    facebook=db.Column(db.String(120), nullable=True)
    instagram=db.Column(db.String(120), nullable=True)



    
    def __init__(self, username, password, email,faculty,graduationyear,programme,department, linkedIn,facebook,instagram):
        self.username = username
        self.set_password(password)
        self.email=email
        self.graduationyear=graduationyear
        self.programme=programme
        self.faculty=faculty
        self.department=department
        self.linkedIn=linkedIn
        self.facebook=facebook
        self.instagram=instagram

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'name':self.name,
            'email':self.email,
            'graduationyear':self.graduationyear,
            'programme':self.programme,
            'faculty':self.faculty,
            'department':self.department,
            'linkedIn':self.linkedIn,
            'facebook':self.facebook,
            'instagram':self.instagram
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

