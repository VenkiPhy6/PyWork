import numpy as np
import pandas as pd
import seaborn as sb
import sklearn
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from sklearn.linear_model import LogisticRegression
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
import statsmodels.api as sm
import pylab as pl
import random as rd
from sklearn import svm,datasets

bl = pd.read_csv("./bankloan.csv")
bl = pd.DataFrame(bl)
print(bl.shape)
print(bl.info())
print(bl.head(3))
plt.plot(bl.default, 'bo'); plt.show()
bl_data = bl.drop(['address','ed','debtinc','employ'],1)
print(bl_data.head(3))
X = bl_data.iloc[:, 0:4]
X.head(3)
y = bl_data.iloc[:,4]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .4)
print(len(X_train))
print(len(X_test))
print(len(y_train))
print(len(y_test))
print(X_train.head(3))
print(X_test.head(3))
print(y_train.head(3))
svcT = svm.SVC(kernel = 'linear', C=1, gamma = 'auto', probability =True).fit(X_train, y_train)
print(svcT)
y_pred = svcT.predict(X_test)
print(y_pred)
print(y_pred.sum())

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

