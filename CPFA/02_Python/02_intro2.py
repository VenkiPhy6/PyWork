#dictionary
pic = {"Bobby":"Dimple", "Sholay":"Hema", "Roja":"Madhoo", "3 Idiot": "Kareena"}
pic
pic["Roja"]
pic["Sholay"] = "Jaya"
pic
pic["Dangal"]="Sana"
pic
pic["Sultan"]="Anushka"
pic
pic.pop("Bobby")
pic
pic.pop("Sholay")
pic
pic.pop("Dangal")
pic
pic.items()
pic.keys()
pic.values()
pic.popitem()
pic
#------------

#list
cinema = ["Bobby", 1974, "Roja", 1990, ["Dimple", "Rishi"]]
cinema[4]
isinstance(cinema[4][1], str)
cinema.__class__
a = [1,2,3,4,5]
b = a
b
b[2] = 0
b
a
c = a[:]
c[3] = 9
c
a
#------------

#sets
set1 = {1,23,23,24}
set1
set2 = {9,10,11}
set1 | set2 #Union
set1[1] #sets don't support indexing
set3 = {1,}
isinstance(set3, set)
a
set4 = set(a)
set4
set1 & set2 #Intersection
set1 - set4 #Stuff in set1 but not set4
set4 - set1 #Stuff in set4 but not set1
a
b = [1,2,3,9,10]
a - b # wont work with set
set4 - set4
set1^set4 #Symmetrical difference: all in a but not in b and all in b but not in a too!
set4^set1
a^b #again unsupported
#-------------

#math
import math
math.pi
math.cos(math.pi)
math.exp(10)
math.log10(1000)
math.log2(10)
math.sinh(0)
math.factorial(1000) # It works!
#----------

#list of lists 
mat1 = [[1,2,3],[2,4,5],[9,11,100]]
mat1[1]
mat1[1][1]
mat1[0,2] #wont work
#-------------


#typecasting
a = 50
isinstance(a,int)
b = str(a)
isinstance(b,str)
c = int(b)
isinstance(c,int)
d = float(c)
d
b = '6ixty9ine'
c= int(b) #wont work now

