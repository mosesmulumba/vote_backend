from app.resources import db

class Election(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(150) , unique=False , nullable=False)
    start_date = db.Column(db.Date , nullable=False)
    end_date = db.Column(db.Date , nullable=False)
    status = db.Column(db.String(50) , nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)

    candidates = db.relationship('Candidate' , backref="election" , lazy=True)