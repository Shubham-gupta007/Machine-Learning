#!/usr/bin/python3

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### make sure you use // when dividing for integer division


#########################################################
### your code goes here ###

#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]

from sklearn import svm
from sklearn.metrics import accuracy_score
clf = svm.SVC(kernel='linear')
t0 = time()
clf.fit(features_train, labels_train)
#print ("training time:", round(time()-t0, 3), "s")
t1 = time()
pred = clf.predict(features_test)
#print ("prediction time:", round(time()-t0, 3), "s")
accuracy = accuracy_score(pred, labels_test)
print("accuracy_score:",accuracy)
#0.98407281001137659
"""
from sklearn import svm
clf = svm.SVC(C=100., kernel='linear')
clf.fit(features_train, labels_train)
labels_predict = clf.predict(features_test)
from sklearn.metrics import accuracy_score
score = accuracy_score(labels_predict,labels_test)
print(score)
"""
#########################################################


