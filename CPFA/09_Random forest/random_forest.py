from sklearn.ensemble import RandomForestClassifier
X = [[0,0], [1,1]]
Y = [0,1]
clf = RandomForestClassifier(n_estimators = 10)
clf = clf.fit(X,Y)
print(clf)
#Do the prediction and stuff

from sklearn.tree import DecicionTreeClassifier
#Try this also and also ExtraTreesClassifier