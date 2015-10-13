#!/bin/python3.4
import requests
import json

class Connection:
	
	def __init__(self, hostname="http://localhost:8080/"):
		self.hostname = hostname

	def query(self, query):
		response = requests.post(self.hostname + "api/v1/datapoints/query", \
		 						 data=json.dumps(query))
		return json.loads(response.text)