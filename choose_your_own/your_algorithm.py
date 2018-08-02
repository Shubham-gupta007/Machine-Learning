#!/usr/bin/python3

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

clf = KNeighborsClassifier(n_neighbors=15, weights='distance')
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

acc = accuracy_score(labels_test, pred)

print(acc)

output:
KNeighborsClassifier
0.92-default
0.928-n_neighbors=5,weights='uniform'
94-n_neighbors=15, weights='distance'


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

clf = RandomForestClassifier(n_estimators=10,min_samples_split=2,max_depth=100 )
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)

print(acc)

#0.916-default
#0.924-n_estimators=15,min_samples_split=2,max_depth=10
#0.928-n_estimators=10,min_samples_split=2,max_depth=100
#0.936-n_estimators=10,min_samples_split=2,max_depth=1000


"""
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

clf = AdaBoostClassifier(base_estimator=None, n_estimators=200, random_state=0)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)

print(acc)

#0.924-default



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
