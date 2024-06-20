from flask_restx import Api , Namespace
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()


# create the namespaces
auth_ns = Namespace('auth', description="Authentication Operation")
member_ns = Namespace('member' , description="Member Operation")
candidate_ns = Namespace('candidate' , description="Candidate Operation")
vote_ns = Namespace('vote' , description="Vote Operation")
election_ns = Namespace('election' , description="Election Operation")
result_ns = Namespace('results' , description="Results Operation")
