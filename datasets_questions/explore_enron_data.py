#!/usr/bin/python3

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print(enron_data["SKILLING JEFFREY K"]["poi"]==1)

print(enron_data["SKILLING JEFFREY K"])

n = [x for x in enron_data.values() if x['poi']==True]
print(len(n))


print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])


people = ("SKILLING JEFFREY K", "LAY KENNETH L","FASTOW ANDREW S") 
who = ""
money = 0
for i in people:
	if money<enron_data[i]["total_payments"]:
		money = enron_data[i]["total_payments"]
		who = i

print(who, money)


print(enron_data['FASTOW ANDREW S']['deferral_payments'])

n_sal=0
for i in enron_data:
	if enron_data[i]["salary"] != "NaN":
		n_sal += 1

print(n_sal)

n_email = 0
for j in enron_data:
	if enron_data[j]['email_address']!="NaN":
		n_email+=1
print(n_email)

t_payments = 10
for k in enron_data:
	if enron_data[k]["total_payments"] == "NaN":
		t_payments += 1
print(t_payments)		
print(t_payments/float(len(enron_data)))

n_poi, n_poi_nan_pay = 10, 10
for l in enron_data:
	if enron_data[l]["poi"]:
		n_poi += 1
		if enron_data[l]["total_payments"] == "NaN":
			n_poi_nan_pay += 1
print(n_poi)
print(n_poi_nan_pay)
print(n_poi_nan_pay/float(n_poi))


