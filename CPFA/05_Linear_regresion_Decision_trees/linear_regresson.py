#Linear regression

import matplotlib.pyplot as plt
from sklearn import linear_model, model_selection
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

#Simple example
"""
reg = linear_model.LinearRegression()
ar = np.array([[[1],[2],[3]], [[2.01],[4.03],[6.04]]])
print(ar.shape)
y = ar[1,:]
x = ar[0,:]
print(reg.fit(x,y))
print('Coefficients: \n',reg.coef_)
xtest = np.array([[4],[5],[6]])
ytest = np.array([[9],[8.5],[14]])
preds = reg.predict(xtest)
print("R2 score: %.2f" % r2_score(ytest, preds))
print("Mean squared error: %.2f" % mean_squared_error(ytest, preds))

er = []
g = 0
for i in range(len(ytest)):
    print("actual=", ytest[i], "observed=", preds[i])
    x = (ytest[i]-preds[i])**2
    er.append(x)
    g = g + x

print(er)
print(g)
print("MSE", g / len(er))

#Plotting
plt.scatter(xtest, ytest)
plt.plot(xtest, preds, color='red')
plt.show()


#Multiple example
reg = linear_model.LinearRegression()
b1 = pd.read_csv('./redataset/bankloan.csv')
b1.head(5)
b1.shape
b1_data = b1.drop(['address','ed','debtinc','default'], 1)
b1_data.head(5)
X = b1_data.iloc[:,0:4]
X.head(3)
y = b1_data.iloc[:,4]
y.head(3)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = .4)
len(X_train)
len(X_test)
len(y_train)
len(y_test)
X_test.head()
y_test.head()
print(reg.fit(X_train, y_train))
print('Coefficients: \n',reg.coef_)
preds = reg.predict(X_test)
#print(preds)
print("R2 score: %.2f" % r2_score(y_test, preds))
print("Mean squared error: %.2f" % mean_squared_error(y_test, preds))
"""

#OLS example
import statsmodels.api as sm
b1 = pd.read_csv('./redataset/bankloan.csv')
y = b1[['income']]
x = b1[['creddebt']]
x = sm.add_constant(x)
mod = sm.OLS(y,x).fit()
mod.summary()
preds = mod.predict(x)
print(preds)