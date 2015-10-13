#!/bin/python3
#
# Example on how to load a Spark DataFrame from KairosDB data.
# Maybe need some adjustments.
#
# Written by @paladini on 09/2015.
# paladini@lisha.ufsc.br 
#
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import *
from connection import Connection
import json

class Dataframe:

	df = None

	def __init__(self, json_data):
		self.df = self.to_dataframe(json_data)

	def to_dataframe(self, json_data):
		data = self.__reduce_data(json_data)
		filename = self.__save_file(data)

		sc = SparkContext("local", appName="JSON to DataFrame")
		sqlContext = SQLContext(sc)
		dataframe = sqlContext.read.json("data.json")
		return dataframe

	def __reduce_data(self, data):
		return map(lambda x: { "name": x["results"][0]["name"], \
							 "values": x["results"][0]["values"]}, data["queries"])

	def __save_file(self, data):
		with open("data.json", "w") as outfile:
			for hostDict in data:
				json.dump(hostDict, outfile)
				outfile.write('\n')
		return "data.json"