from app.resources import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    post = db.Column(db.String(150), unique=False, nullable=False)