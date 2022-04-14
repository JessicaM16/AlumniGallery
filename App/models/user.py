from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    email=db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    graduationyear=db.Column(db.Integer, nullable=False)
    programme=db.Column(db.String(120),nullable=False)
    faculty=db.Column(db.String(120),nullable=False)
    department=db.Column(db.String(120),nullable=False)
    #socialmedia=db.Column(db.String(120),nullable=False)
    linkedIn=db.Column(db.String, nullable=False)
    facebook=db.Column(db.String, nullable=True)
    instagram=db.Column(db.String, nullable=True)



    
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

