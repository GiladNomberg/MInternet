import pandas as pd
import re
from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

customers = []
df = pd.read_csv('churn_case_data.csv', sep = ';')
for index, row in df.iterrows():
	customer_dict = {}
	customer_dict['id'] = row['id']
	customer_dict['gender'] = row['gender']
	customer_dict['segment'] = row['segment']
	customer_dict['years_customer'] = row['years_customer']
	customer_dict['no_of_complaints'] = row['no_of_complaints']
	customer_dict['contract_value'] = row['contract_value']
	customers.append(customer_dict)	
	

@app.route("/")
def get_data():
	response_object = {}
	_id = request.args.get("id")
	isDigit = re.search("\d", _id)
	if isDigit:
		segment_id = int(_id[isDigit.start()])
	else:
		segment_id = 0
	if(segment_id != 0):
		specificCustomers = []
		for customer in customers:
			if(customer["segment"] == segment_id):
				specificCustomers.append(customer)
		response_object["data"] = specificCustomers
		add_meta_data(response_object, specificCustomers)	
	else:
		response_object["data"] = customers
		add_meta_data(response_object, customers)
		
	return jsonify(response_object)

	
def add_meta_data(response_object, customers):
	sum_years = 0
	sum_complains = 0
	number_of_customers = 0
	
	for customer in customers:
		sum_years += customer["years_customer"]
		sum_complains += customer["no_of_complaints"]
		number_of_customers += 1
	
	average_years = sum_years / number_of_customers
	average_years = ("%.4f" % average_years)
	average_complains = sum_complains / number_of_customers
	average_complains = ("%.4f" % average_complains)
	response_object["years"] = average_years
	response_object["complains"] = average_complains

if __name__ == "__main__":
	app.run()
