from .resources import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    vote = db.relationship('Vote', backref="user" , lazy=True)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    post = db.Column(db.String(150), unique=True, nullable=False)
    vote = db.relationship('Vote', backref="candidate" , lazy=True)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())