from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db



class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    email=db.Column(db.String(120),unique=True, nullable=False)
    experience = db.Column(db.String, nullable=False)
    details=db.Column(db.String, nullable=False)

    
    def toDict(self):
        return{
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'email': self.email,
            'experience': self.experience,
            'details': self.details
        }
    
    

