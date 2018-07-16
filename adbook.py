from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Contact(Resource):

	def post(self):

	def get(self, name):

	def put(self, name):

	def delete(self, name):

api.add_resource(Contact, "/contact/<string:name>")

if __name__ == "__main__":
	app.run()