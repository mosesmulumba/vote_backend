from app.resources import db

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    election_id = db.Column(db.Integer , db.ForeignKey('election.id') , nullable=False )
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User' , backref='user_votes')
    candidate = db.relationship('Candidate' , backref='votes')
    election = db.relationship('Election' , backref='votes')