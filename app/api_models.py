from flask_restx import fields
from .resources import *

login_model = auth_ns.model("Login",{
    "username": fields.String(required=True),
    "password" : fields.String(required=True),
})

members_model = member_ns.model("User", {
    "id": fields.Integer,
    "username" : fields.String,
    "password" : fields.String
})

member_model_input = member_ns.model("MemberInput",{
    "username" : fields.String,
    "password" : fields.String
})


vote_model = vote_ns.model("Votes_model",{
    "id": fields.Integer,
    "user_id": fields.Integer,
    "candidate_id": fields.Integer,
    "timestamp": fields.DateTime
})

vote_model_input= vote_ns.model("Vote_Input",{
    "user_id": fields.Integer,
    "candidate_id": fields.Integer,
    "election_id": fields.Integer
})

candidate_model = candidate_ns.model("Candidate" ,{
    "id": fields.Integer,
    "name": fields.String,
    "post": fields.String,
    "votes": fields.Nested(vote_model)
})

candidate_model_input = candidate_ns.model("Candidate_Input",{
    "name": fields.String,
    "post": fields.String
})

election_model = election_ns.model("ElectionModel",{
   'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
    'start_date': fields.Date(required=True),
    'end_date': fields.Date(required=True),
    'status': fields.String(required=True),
    'candidate_id': fields.Integer(required=True)
})

election_model_input = election_ns.model("ElectionModel_Input",{
    "name" : fields.String,
    "start_date" : fields.Date,
    "end_date" : fields.Date,
    "candidate_id": fields.Integer
})

