import flask_restful as restful
import json
from flask import Flask, request

from db_orm import *	# config_json imported here

##########################################################################################

# API in the end - search "post_test" to jump
# service method classes
class POST_TEST(restful.Resource):
	def post(self):
		data = request.get_json()
		t = data.get('key', 1)
		recs = session.query(PollData).filter().all()
		data = []
		# function to serialize recs
		for rec in recs:
			data.append({'id': rec.id, 'poll_name': rec.poll_name})
		return {"res": "post test called", "data": data}


class GET_TEST(restful.Resource):
	def get(self):
		return {"res": "get test called"}




##########################################################################################
# APIs
app = Flask(__name__)
api = restful.Api(app)

api.add_resource(POST_TEST, '/post_test')
api.add_resource(GET_TEST, '/get_test')
