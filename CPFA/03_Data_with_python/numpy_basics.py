import numpy as np
data1 = [[1,2,3,4],[5,6,7,8]]
data1
len(data1)
data1.__class__
np.zeros((3,6))
k = np.arange(15)
k
k.__class__
k.dtype
isinstance(k, tuple)
isinstance(k, list)
list(k)
isinstance(k, list)
k1 = k.reshape(3,5)
k1
k1.T #transpose
np.exp(k1)
k2 = np.sqrt(k1)
k2
np.ceil(k2)
np.ceil(-3.978)
np.round(k2,2)
np.floor(k2)
x1 = [4,2,1]
x2 = [2,2,2]
np.greater_equal(x1,x2)
x3 = np.array([4,2,1])
x4 = np.array([2,2,2])
np.greater_equal(x3,x4)
arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
arr
arr.mean()
np.mean(arr)
arr.std()
np.std(arr)

x=np.array([1,2,3,4])
y=x
x is y
id(x), id(y)
x[0] = 9
y
x[0] = 1
x
z = x[:]
z
x is z
id(x), id(z)
x[0] = 8
z
x= np.array([1,2,3,4])
y=x.copy()
x is y
id(x), id(y)
x[0] = 9
x
y