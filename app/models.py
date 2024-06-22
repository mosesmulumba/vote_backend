from .resources import db
import bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(150), unique=True, nullable=False  , default='')
    email = db.Column(db.String(256) , unique=True , default='')
    password = db.Column(db.String(150), unique=True ,  nullable=False)
    date_created = db.Column(db.DateTime , default=db.func.current_timestamp())
    verified = db.Column(db.Boolean , nullable=False , default=False)
    role = db.Column(db.String(80) , nullable=False , default='admin')

    def __init__(self , username , email , password):
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def password_is_valid(self , password):
        return bcrypt().check_password_hash(self.password , password)
    
    def generate_token(self , user):
        expiry = timedelta(days=1)
        return create_access_token(user , expires_delta=expiry)
    


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    post = db.Column(db.String(150), unique=False, nullable=False)

class Election(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(150) , unique=False , nullable=False)
    start_date = db.Column(db.Date , nullable=False)
    end_date = db.Column(db.Date , nullable=False)
    status = db.Column(db.String(50) , nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)

    candidates = db.relationship('Candidate' , backref="election" , lazy=True)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    election_id = db.Column(db.Integer , db.ForeignKey('election.id') , nullable=False )
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User' , backref='user_votes')
    candidate = db.relationship('Candidate' , backref='votes')
    election = db.relationship('Election' , backref='votes')