
""" 
	Server	: To handle Restful api and communicate between Parser and Clients request.
	API 	: Only implements GET, that suits our requirement
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
from app.Parser import Parser
from app.constants import STATUS_CODE , CROSS_ORIGIN_POLICY

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

# API GET()
class IntentClassification(Resource):
    def get(self, query):
    	if query is None:
    		return {} , STATUS_CODE["BAD_REQUEST"] , CROSS_ORIGIN_POLICY
    	intent = Parser.parseIntent(query)
    	if intent is None:
    		return {} , STATUS_CODE["FAIL"] , CROSS_ORIGIN_POLICY
    	return intent , STATUS_CODE["SUCCESS"] , CROSS_ORIGIN_POLICY

# API endpoint
api.add_resource(IntentClassification, "/intent/<string:query>")


# Start Server
if __name__ == '__main__':
    app.run(debug=False)