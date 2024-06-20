from .resources import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), unique=True ,  nullable=False)

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