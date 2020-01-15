import flask_restful as restful
import json
from flask import Flask, request
from flask_cors import CORS

from db_orm import *	# config_json imported here

##########################################################################################

# API in the end - search "post_test" to jump

################# API RESPONSE FORMAT #################
# {
# 	'success': True,
# 	'message': '',
# 	'error_code': 12,	# if success == False
# 	'data': []
# 	'count': 0
# }
################# API RESPONSE FORMAT #################

# service method classes
class POST_TEST(restful.Resource):
	def post(self):
		data = request.get_json()
		t = data.get('key', 1)
		recs = session.query(PollData).filter().all()
		# data = []
		# function to serialize recs
		# for rec in recs:
		# 	data.append({'id': rec.id, 'poll_name': rec.poll_name})
		# print( json.dumps(recs, cls=AlchemyEncoder))
		recs = orm_list(recs)
		return {'success': True, 'message': 'post test called', 'data': recs}


class GET_TEST(restful.Resource):
	def get(self):
		return {'success': True, 'message': 'get test called', 'data': data}


class CreateUser(restful.Resource):
	def post(self):
		data = request.get_json()
		
		if len(session.query(User).filter(User.email == data['email']).all()):
			return {'success': False, 'message': 'Email Already exists', 'error_code': 1}

		orm_rec = User(
            user_name = data['user_name'],
            email = data['email'],
            password = data['password'])
		
		try:
			session.add(orm_rec)
			session.commit()
			return {'success': True, 'message': 'New User Created', 'data': orm_dict(orm_rec)}
		except Exception as e:
			return {'success': False, 'message': 'Some Error Occured', 'error_code': 2}		


class LoginUser(restful.Resource):
	def post(self):
		data = request.get_json()
		try:
			orm_rec = session.query(User).filter(User.email == data['email'], User.password == data['password']).one()
			return {'success': True, 'message': 'Login Successful', 'data': orm_dict(orm_rec)}
		except Exception as e:
			return {'success': False, 'message': 'Email and Password did not match', 'error_code': 1}


class NewPoll(restful.Resource):
	def post(self):
		data = request.get_json()
		print(data)

		orm_rec = PollData(
            question = data['question'],
            question_type = data['question_type'],
            options = data['options'],
            answer_limit = data['answer_limit'],
            participant_count = data['participant_count'],
            timer = data['timer'],
            show_result_on = data['show_result_on'],
            is_anonymous = data['is_anonymous'],
            created_on = datetime.datetime.now(),
            id_user = data['id_user'])
        # print (orm_rec)

		session.add(orm_rec)
		session.commit()
		# print(orm_list(orm_rec))
		return {'success': True, 'message': 'New poll created', 'data': orm_dict(orm_rec)}


class GetPollData(restful.Resource):
	def post(self):
		data = request.get_json()

		# .all() returns list && .one() returns dict
		try:
			orm_rec = session.query(PollData).filter(PollData.id == data['id']).one()
			return {'success': True, 'data': orm_dict(orm_rec)}
		except Exception as e:
			return {'success': False, 'message': 'No Record Found'}


class GetUserPolls(restful.Resource):
	def post(self):
		data = request.get_json()

		orm_rec = session.query(PollData).filter(PollData.owner == data['owner']).all()
		
		return {'success': True, 'data': orm_list(orm_rec), 'count': len(orm_rec)}


class GetAttemptCount(restful.Resource):
	def post(self):
		data = request.get_json()

		orm_rec = session.query(PollAnswers.answered_by, func.count(PollAnswers.answered_by))\
						.filter(PollAnswers.id_poll_data == data['id_poll_data'])\
						.group_by(PollAnswers.answered_by).all()
		# print(orm_rec)
		return {'success': True, 'data': len(orm_rec)}


class HasAttempted(restful.Resource):
	def post(self):
		data = request.get_json()

		orm_rec = session.query(PollAnswers).filter(PollAnswers.id_poll_data == data['poll_id'], 
													PollAnswers.answered_by == str(data['user_id'])).all()
		# print(orm_rec)
		return {'success': True, 'data': True if len(orm_rec) else False}


#TODO
class AnswerPoll(restful.Resource):
	def post(self):
		data = request.get_json()

		# User
		# PollAnswers
		orm_rec = session.query(PollData).filter(PollData.id == data['id']).all()
		
		return {'success': True, 'data': orm_list(orm_rec)}


#TODO
class GetPollResults(restful.Resource):
	def post(self):
		data = request.get_json()

		# User
		# PollAnswers
		orm_rec = session.query(PollData).filter(PollData.id == data['poll_id']).all()
		
		return {'success': True, 'data': orm_list(orm_rec)}





##########################################################################################
# APIs
app = Flask(__name__)
api = restful.Api(app)

CORS(app, max_age=1000)

api.add_resource(POST_TEST, '/post_test')
api.add_resource(GET_TEST, '/get_test')

api.add_resource(CreateUser, '/create_user')
api.add_resource(LoginUser, '/login_user')
api.add_resource(NewPoll, '/new_poll')
api.add_resource(GetPollData, '/get_poll_data')
api.add_resource(GetUserPolls, '/get_user_polls')
api.add_resource(GetAttemptCount, '/get_attempt_count')
api.add_resource(HasAttempted, '/has_attempted')
api.add_resource(AnswerPoll, '/answer_poll')
api.add_resource(GetPollResults, '/get_poll_results')
