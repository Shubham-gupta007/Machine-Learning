#!/usr/bin/python3

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

a,b = 0,0
for point in data:
    salary = point[0]
    if a< salary:
        a = salary
    bonus = point[1]
    if b < bonus:
	    b = bonus
    print(a, b)
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.savefig("enron.png")
matplotlib.pyplot.show()