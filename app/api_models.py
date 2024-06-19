from flask_restx import fields
from .resources import api

members_model = api.model("User", {
    "id": fields.Integer,
    "username" : fields.String,
    "password" : fields.String
})

member_model_input = api.model("MemberInput",{
    "username" : fields.String,
    "password" : fields.String
})

candidate_model = api.model("Candidate" ,{
    "id": fields.Integer,
    "name": fields.String,
    "post": fields.String
})

candidate_model_input = api.model("Candidate_Input",{
    "name": fields.String,
    "post": fields.String
})

vote_model = api.model("Votes_model",{
    "id": fields.Integer,
    "user_id": fields.Integer,
    "candidate_id": fields.Integer,
    "timestamp": fields.DateTime
})

vote_model_input= api.model("Vote_Input",{
    "user_id": fields.Integer,
    "candidate_id": fields.Integer
})
