from flask_restx import Namespace , Resource
from .resources import db
from .api_models import members_model , member_model_input , candidate_model_input , candidate_model , vote_model , vote_model_input
from .models import User , Candidate , Vote

ns = Namespace("api")

@ns.route("/members")
class Members_LIST_API(Resource):
    @ns.marshal_list_with(members_model)
    def get(self):
        return User.query.all()
    
    @ns.expect(member_model_input)
    @ns.marshal_with(members_model)
    def post(self):
        student = User(username=ns.payload['username'], password=ns.payload['password'])
        db.session.add(student)
        db.session.commit()
        return student
    
@ns.route("/member/<int:id>")
class Member_ByID(Resource):
    @ns.marshal_with(members_model)
    def get(self, id):
        student = User.query.get(id)
        return student
    
    @ns.expect(member_model_input)
    @ns.marshal_with(members_model)
    def put(self, id):
        student = User.query.get(id)
        student.username = ns.payload['username']
        student.password = ns.payload['password']
        db.session.commit()
        return student
    
    def delete(self, id):
        student = User.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return ({"message": "Student with id {id} has been deleted."}), 204


@ns.route('/candidates')
class Candidate_API_LIST(Resource):
    @ns.marshal_list_with(candidate_model)
    def get(self):
        return Candidate.query.all()
    
    @ns.expect(candidate_model_input)
    @ns.marshal_with(candidate_model)
    def post(self):
        candidate = Candidate(name=ns.payload['name'], post=ns.payload['post'])
        db.session.add(candidate)
        db.session.commit()
        return candidate
    
@ns.route('/candidate/<int:id>')
class Single_Candidate(Resource):
    @ns.marshal_with(candidate_model)
    def get(self, id):
        candidate = Candidate.query.get(id)
        return candidate
    
    @ns.expect(candidate_model_input)
    @ns.marshal_with(candidate_model)
    def put(self, id):
        candidate = Candidate.query.get(id)
        candidate.name = ns.payload['name']
        candidate.post = ns.payload['post']
        db.session.commit()
        return candidate
    
    def delete(self, id):
        candidate = Candidate.query.get(id)
        db.session.delete(candidate)
        db.session.commit()
        return  {"You have successfully deleted user {candidate.name}"}, 204

@ns.route('/votes')
class Votes(Resource):
    @ns.marshal_list_with(vote_model)
    def get(self):
        return Vote.query.all()
    
    @ns.expect(vote_model_input)
    @ns.marshal_with(vote_model)
    def post(self):
        vote = Vote(user_id=ns.payload['user_id'], candidate_id=ns.payload['candidate_id'])
        db.session.add(vote)
        db.session.commit()
        return vote
    
