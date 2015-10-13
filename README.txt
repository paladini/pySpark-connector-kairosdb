==========================
pySpark-connector-kairosdb
==========================

pySpark-connector-kairosdb provides you an easy way to get data from KairosDB and make it available on Spark as a DataFrame. It's simple as that::

    #!/usr/bin/env python

    # sconnk means "py(S)park-(CONN)ector-(K)airosdb"
    from sconnk import Connection, Dataframe

    query_data = {
			"start_relative": { "value": "5", "unit": "years" },
			"metrics": [{ "name": "test_", "limit": 5 },
						{ "name": "DP_058424", "limit": 10 },
						{ "name": "teste_gzip", "limit": 5 },
						{ "name": "DP_063321", "limit": 10 }]
	}

	# Creating a connection with KairosDB database (in the given address).
	conn = Connection("http://localhost:8080/")

	# Performing our query on KairosDB.
	json_data = conn.query(query_data)

	# Creating a new Dataframe object passing the JSON returned by KairosDB API.
	df = Dataframe(json_data).df

	# Print the dataframe.
	df.show()

Remember this's a ALPHA module without good documentation, examples and even well implemented features. We've a long highway to cross.

Future
=========

This module is in development and we've the following plannings for the future of this module:

* Write good documentation
* Write tests - a lot of them.
* Add support to RDD
* Don't write to JSON file in order to parse it in Spark.