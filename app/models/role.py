from app.resources import db
from .student import User

class Role(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(256) , nullable=False)

    users = db.relationship('User' , secondary='user_role' , backref='roles')

    def __init__(self, name):
        self.name = name