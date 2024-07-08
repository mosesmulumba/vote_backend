from flask  import Flask
from .resources import api , db , auth_ns , member_ns , candidate_ns , vote_ns , election_ns , result_ns 
from .routes import *
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager 
from flask_cors import CORS


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user_evote:LINum-mh0ses1234@localhost/evote"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "mosesmulumba@94"

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

api.init_app(app)

api.add_namespace(auth_ns)
api.add_namespace(member_ns)
api.add_namespace(candidate_ns)
api.add_namespace(vote_ns)
api.add_namespace(result_ns)
api.add_namespace(election_ns)

db.init_app(app)

jwt = JWTManager(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
 
