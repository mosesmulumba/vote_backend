from app.resources import db
from app.models.student import User
from app.models.role import Role

class UserRole(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey(User.id))
    role_id = db.Column(db.Integer , db.ForeignKey(Role.id))