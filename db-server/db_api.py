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


# TODO
class CreateUser(restful.Resource):
	def post(self):
		data = request.get_json()
		# User
		return {'success': True, 'message': 'New poll created', 'data': orm_list(orm_rec)}


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
            owner = data['owner'])
        # print (orm_rec)

		session.add(orm_rec)
		session.commit()
		# print(orm_list(orm_rec))
		return {'success': True, 'message': 'New poll created', 'data': orm_dict(orm_rec)}


class GetPollData(restful.Resource):
	def post(self):
		data = request.get_json()

		# .all() returns list && .one() returns dict
		orm_rec = session.query(PollData).filter(PollData.id == data['id']).one()
		
		return {'success': True, 'data': orm_dict(orm_rec)}


class GetUserPolls(restful.Resource):
	def post(self):
		data = request.get_json()

		orm_rec = session.query(PollData).filter(PollData.owner == data['owner']).all()
		
		return {'success': True, 'data': orm_list(orm_rec), 'count': len(orm_rec)}


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
		orm_rec = session.query(PollData).filter(PollData.id == data['id']).all()
		
		return {'success': True, 'data': orm_list(orm_rec)}





##########################################################################################
# APIs
app = Flask(__name__)
api = restful.Api(app)

CORS(app, max_age=1000)

api.add_resource(POST_TEST, '/post_test')
api.add_resource(GET_TEST, '/get_test')

api.add_resource(CreateUser, '/create_user')
api.add_resource(NewPoll, '/new_poll')
api.add_resource(GetPollData, '/get_poll_data')
api.add_resource(GetUserPolls, '/get_user_polls')
api.add_resource(AnswerPoll, '/answer_poll')
api.add_resource(GetPollResults, '/get_poll_results')
