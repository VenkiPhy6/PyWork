import sklearn.datasets as datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus



iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
y = iris.target #There are 3 categories possible. With the columns in df we have to predict whcih category the flower belongs to.
#print(y)
#print(df.head(6))
#print(df.columns)

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size = .4)
#len(X_train)
##len(X_test)
#len(y_train)
#len(y_test)
#X_test.head()
#y_test.head()

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

treepred = dtree.predict(X_test)
#print(treepred)
#print(y_test)

#making confusion matrix
cm_deci1 = pd.crosstab(treepred, y_test, rownames = ['True'], colnames = ['Predicted'], margins = True)
print(cm_deci1) 

dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data, filled = True, rounded = True, special_characters = True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#Image(graph.create_png())
graph.write_png('tree.png')