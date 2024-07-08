from app.resources import db
from flask_bcrypt import bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(150), unique=True, nullable=False  , default='')
    email = db.Column(db.String(256) , unique=True , default='')
    password = db.Column(db.String(150), unique=True ,  nullable=False)
    date_created = db.Column(db.DateTime , default=db.func.current_timestamp())
    verified = db.Column(db.Boolean , nullable=False , default=False)
    # role = db.Column(db.String(80) , nullable=False , default='admin')

    def __init__(self , username , email , password):
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def password_is_valid(self , password):
        return bcrypt().check_password_hash(self.password , password)
    
    def generate_token(self , user):
        expiry = timedelta(days=1)
        return create_access_token(user , expires_delta=expiry)