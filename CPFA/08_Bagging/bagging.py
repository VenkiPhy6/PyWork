from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

bagging = BaggingClassifier(KNeighborsClassifier(), max_features = .5, max_samples = .5)
bagging
bl = pd.read_csv("./bankloan.csv")
bl = pd.DataFrame(bl)
print(bl.shape)
print(bl.info())
print(bl.head(3))
bl_data = bl.drop(['address','ed','debtinc','employ'],1)
print(bl_data.head(3))
X = bl_data.iloc[:, 1:4]
y = bl_data.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .4)
bag_fit = bagging.fit(X_train, y_train)
print(bag_fit)
y_pred = bag_fit.predict(X_test)
print(y_pred)
#print(y_pred.sum())
"""
from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)
print(classification_report(y_test, y_pred))

#ROC curve
preds1 = svcT.predict_proba(X_test)[:,1]
fpr1, tpr1, thresholds1 = metrics.roc_curve(y_test, preds1) 
fpr1
tpr1
thresholds1
df1 = pd.DataFrame(dict(fpr = fpr1, tpr = tpr1))
aucl = auc(fpr1, tpr1)
plt.figure()
lw = 2
plt.plot(fpr1, tpr1, color = 'darkorange', lw = lw, label = "ROC curve (area = %.2f)" % aucl)
plt.plot([0,1], [0,1], color = 'navy', lw = lw, linestyle = '--')
plt.xlim([0.0,1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic example')
plt.legend(loc = 'lower right')
plt.show()

"""