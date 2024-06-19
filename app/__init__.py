from flask  import Flask
from .resources import api , db
from .routes import ns
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://moses:#BAliba1234@localhost/evote"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api.init_app(app)
db.init_app(app)
api.add_namespace(ns)
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
 
