#!/bin/python

# Import classes from the pySpark-connector-kairosdb library.
from sconnk import Connection, Dataframe

# Import needed Spark classes.
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import *

# Make your desired query.
# Refer to http://kairosdb.github.io/docs/build/html/restapi/QueryMetrics.html
query_data = {
	"start_relative": { "value": "5", "unit": "years" },
	"metrics": [
		{ "name": "test_", "limit": 5 },
		{ "name": "DP_058424", "limit": 10 },
		{ "name": "teste_gzip", "limit": 5 },
		{ "name": "DP_063321", "limit": 10 }
	]
}

# Creating a connection with KairosDB database (in the given address).
conn = Connection("http://localhost:8080/")

# Performing our query on KairosDB.
json_data = conn.query(query_data)

# Creating a new Dataframe object passing the JSON returned by KairosDB API.
df = Dataframe(json_data).df

# Print the dataframe.
df.show()