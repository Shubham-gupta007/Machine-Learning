#!/usr/bin/python3


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn import tree
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix, precision_score, recall_score, classification_report
from sklearn.metrics import accuracy_score

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state = 42)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)


acc = clf.score(features_test, labels_test)
print("accuracy:", acc)


pred = clf.predict(features_test)

num_of_pois = 0
for preds in pred:
    if preds == 1:
	    num_of_pois +=1
print(num_of_pois)
print(len(pred))

true_positives = 0
false_positives = 0
false_negatives = 0
for preds,actual in zip(pred, labels_test):
    if preds == actual and actual == 1:
	    true_positives += 1
    elif preds == 1 and actual == 0:
        false_positives += 1
    elif preds == 0 and actual ==1:
        false_negatives +=1
		
print("true_positives: ", true_positives)		
print("false_positives", false_positives)
print("false_negatives", false_negatives)

print("precision_score_true",true_positives/(true_positives+ false_positives))
print("recall_poi:",true_positives/(true_positives+ false_negatives))