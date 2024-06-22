from flask import jsonify , request
from functools import wraps
from flask_jwt_extended import create_access_token ,jwt_required , get_jwt_identity , verify_jwt_in_request
from flask_restx import  Resource
from .resources import db , api , auth_ns, member_ns, candidate_ns, election_ns, vote_ns , result_ns
from .api_models import members_model , member_model_input , candidate_model_input , candidate_model , vote_model , vote_model_input , election_model , election_model_input , login_model
from .models import User , Candidate , Vote , Election


# creating the role custom function to check if one is admin
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args , **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_identity()
        if claims['role'] != 'admin':
            return jsonify({'msg':'Admins only allowed'}) , 403
        return fn(*args , **kwargs)
    return wrapper

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = auth_ns.payload
        user = User.query.filter_by(username=data['username']).first()
        if user and user.email == data['email']:
            access_token = create_access_token(identity={'id':user.id , 'role':user.role})
            result_access_token = [access_token]
            return jsonify({
                "access_token" :result_access_token , 
                "username" : user.username , 
                "user-password" :user.password,
                "user_email" : user.email,
                "role" : user.role,
                "date_created": user.date_created
                })
        return jsonify({'msg': 'Bad Username or email'}), 401


# Error Handling
@api.errorhandler
def default_error_handler(error):
    return {'message': str(error)}, 500

class BadRequestError(Exception):
    pass

@api.errorhandler(BadRequestError)
def handle_bad_request(error):
    return {'message': 'A bad request error occurred'}, 400


@member_ns.route("")
class Members_LIST_API(Resource):
    # @jwt_required()
    # @admin_required
    @member_ns.marshal_list_with(members_model)
    def get(self):
        return User.query.all()

    # @jwt_required()
    # @admin_required
    @member_ns.expect(member_model_input)
    @member_ns.marshal_with(members_model)
    def post(self):
        student = User(username=member_ns.payload['username'],
                       email=member_ns.payload['email'],
                       password=member_ns.payload['password']
                       )
        db.session.add(student)
        db.session.commit()
        return student
    
@member_ns.route("/<int:id>")
class Member_ByID(Resource):
    # @jwt_required()
    # @admin_required
    @member_ns.marshal_with(members_model)
    def get(self, id):
        student = User.query.get(id)
        return student
    
    # @jwt_required()
    # @admin_required
    @member_ns.expect(member_model_input)
    @member_ns.marshal_with(members_model)
    def put(self, id):
        student = User.query.get(id)
        student.username = member_ns.payload['username']
        student.email = member_ns.payload['email']
        student.password = member_ns.payload['password']
        db.session.commit()
        return student
    
    # @jwt_required()
    # @admin_required
    def delete(self, id):
        student = User.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return ({"message": "Student with id {id} has been deleted."}), 204


@candidate_ns.route('')
class Candidate_API_LIST(Resource):
    # @jwt_required()
    # @admin_required
    @candidate_ns.marshal_list_with(candidate_model)
    def get(self):
        return Candidate.query.all()
    
    # @jwt_required()
    # @admin_required
    @candidate_ns.expect(candidate_model_input)
    @candidate_ns.marshal_with(candidate_model)
    def post(self):
        candidate = Candidate(name=candidate_ns.payload['name'], post=candidate_ns.payload['post'])
        db.session.add(candidate)
        db.session.commit()
        return candidate
    
@candidate_ns.route('/<int:id>')
class Single_Candidate(Resource):
    @candidate_ns.marshal_with(candidate_model)
    def get(self, id):
        candidate = Candidate.query.get(id)
        return candidate
    
    # @jwt_required()
    # @admin_required
    @candidate_ns.expect(candidate_model_input)
    @candidate_ns.marshal_with(candidate_model)
    def put(self, id):
        candidate = Candidate.query.get(id)
        candidate.name = candidate_ns.payload['name']
        candidate.post = candidate_ns.payload['post']
        db.session.commit()
        return candidate
    

    # @jwt_required()
    # @admin_required
    def delete(self, id):
        candidate = Candidate.query.get(id)
        db.session.delete(candidate)
        db.session.commit()
        return  {"You have successfully deleted user {candidate.name}"}, 204

@vote_ns.route('')
class Votes(Resource):
    @vote_ns.marshal_list_with(vote_model)
    def get(self):
        return Vote.query.all()
    
    @vote_ns.expect(vote_model_input)
    @vote_ns.marshal_with(vote_model)
    def post(self):
        vote = Vote(
            user_id=vote_ns.payload['user_id'],
            candidate_id=vote_ns.payload['candidate_id'] , 
            election_id=vote_ns.payload['election_id']
            )
        db.session.add(vote)
        db.session.commit()
        return vote
    

class Election_Results(Resource):
    # @jwt_required()
    # @admin_required
    def get(self):
        # results = db.session.query(
        #     Vote.candidate_id , db.func.count(Vote.id).label('votes')
        # ).group_by(Vote.candidate_id).all()

        results = db.session.query(
            Candidate.id , Candidate.name , db.func.count(Vote.id).label('votes')
        ).join(Vote, Candidate.id == Vote.candidate_id).group_by(Candidate.id).all()

        # results_dict = [{'candidate_id': r.candidate_id, 'votes': r.votes} for r in results]
        results_dict = [{'Candidate_id': r.id , 'Candidate_name': r.name , "Votes": r.votes} for r in results]
        return jsonify(results_dict)
    
result_ns.add_resource(Election_Results, '')

@election_ns.route('')
class Election_API(Resource):
    # @jwt_required()
    # @admin_required
    @election_ns.marshal_list_with(election_model)
    def get(self):
        return Election.query.all()
    

    @election_ns.expect(election_model_input)
    @election_ns.marshal_with(election_model)
    def post(self):
        data = election_ns.payload
        new_election = Election(name=data['name'], 
                                start_date=data['start_date'],
                                end_date=data['end_date'],
                                status='active',
                                candidate_id=data['candidate_id'])
        db.session.add(new_election)
        db.session.commit()
        return new_election , 201
    
    # @jwt_required()
    # @admin_required
    def delete(self):
        active_election = Election.query.filter_by(status='active').first()
        if not active_election:
            election_ns.abort(404, 'No active election')

        if active_election.status == 'active':
            db.session.delete(active_election)
        db.session.commit()
        return {'message' : 'Election closed succefully'} , 200
    
    

