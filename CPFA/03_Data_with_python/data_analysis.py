import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from scipy import stats


#Creating & Exploring Data Frames
grades = pd.read_csv("D:/Personal files/Academics/Data_Science_related/CPFA/03_Data_with_python/data/grades.csv")
grades
grades = pd.DataFrame(grades) #This is sorta redundant since read_csv achieves this
grades
grades.shape
grades.head(3)
grades.tail(6)
cs2m = pd.read_csv("D:/Personal files/Academics/Data_Science_related/CPFA/03_Data_with_python/data/cs2m.csv")
len(grades.id) #access variable
grades['quiz1'].dtype
grades.dtypes
grades.info #These two give different output
grades.info()
cs2m.columns
#---------------------------

#Finding dupes
grades.firstname.shape
grades.firstname.unique().shape
duplicate_count = grades.firstname.shape[0] - grades.firstname.unique().shape[0]
duplicate_count
grades.grade.shape
grades.grade.unique().shape
#----------------------------

#Descriptive stats
grades.describe()
grades.quiz1.describe()
grades.final.describe()
cs2m.describe()
grades.ethnicity.value_counts()
grades.final.min()
grades.final.max()
grades.final.sum()
grades.final.skew()
grades.final.std()
grades.final.kurtosis()
grades.final.kurt()
grades.final.count()
grades.final.mean()
grades.final.quantile(.25)
grades.final.quantile(.5)
grades.final.quantile(.1)
grades.skew()
grades.quiz1.skew()
stats.describe(cs2m.Age)
stats.sem(cs2m.Age)
cs2m.Age.std()
stats.iqr(cs2m.Age)
#----------------------------

#Subsetting
#See : 
#https://stackoverflow.com/questions/11285613/selecting-multiple-columns-in-a-pandas-dataframe
grades[10:13]
grades[10:13]
grades.quiz1[10:13]
grades.iloc[10:13,0:2]
grades[['quiz1','quiz2']][10:12]
#grades.loc - try it
#Also try drop
grades.ix[0:3,0:4] #deprecation warning
grades.ix[:,0:4].head(3) #Different way
#New dataframe after subsetting
grades1 = grades[["quiz1","gpa","final"]]
grades1.head(3)
cs2m1 = cs2m[10:20]
cs2m1.head(3)
#Condition based subsetting
cs2m.BP.compress((cs2m.BP <= 170))
cs2m_140 = cs2m[cs2m.BP >140]
cs2m_140
#----------------------------

#Sampling
cs2m.sample(5)
grades.sample(10)
#---------------------------

#Plotting
#Histogram
plt.hist(grades.total, bins='auto') #total is the name of a column
plt.hist(grades.total, bins='auto', facecolor = 'red')
plt.xlabel('total')
plt.ylabel('Count')
plt.title('Histogram of total')
grades.hist('total') #another way
#Boxplot - Use it when trying to studying continuous data over several categories
cs2m.boxplot('BP')
cs2m.boxplot()
cs2m.boxplot(by = 'Prgnt')

BP = cs2m['BP']
props1 = {"boxes": "red"} #dict(boxes="red") This way you are using less quotes
cx = BP.plot.box(color=props1)

df = grades[['total','ethnicity']]
df.boxplot(by='ethnicity')

#scatterplot
plt.xlabel('Age')
plt.ylabel('BP')
plt.scatter(cs2m['Age'],cs2m['BP'])

#Using seaborn - You can eve see confidence intervals!
seaborn.pairplot(cs2m, vars = ['Age', 'BP', 'Chlstrl'], kind='reg')
#--------------------------

#Merging
grades1 = grades[["quiz1","gpa","final"]]
grades2 = grades[["ethnicity"]]
#have to figure out how to do
#--------------------------

#Making and deleting columns/variables
#need to look up np.where
cs2m['sqrtBP']=np.sqrt(cs2m.BP)    
cs2m.columns
del cs2m['sqrtBP']
cs2m.columns
#-------------------------

#Grouping
cs2m.Age.groupby(cs2m.Prgnt).mean()
cs2m.Age.groupby(cs2m.Prgnt).describe()
grades.total.groupby(grades.ethnicity).describe()
k = grades.groupby(['ethnicity', 'gender'])
grades_total = k['total']
grades_total.agg('mean')
grades_total.agg('describe')
k1 = grades.groupby(['gender', 'ethnicity'])
grades_total1 = k1['total']
grades_total1.agg('mean')
grades_total1.agg('describe')
#------------------------

#Tabulation
pd.crosstab(grades.ethnicity, grades.gender, margins = 1)
pd.crosstab(cs2m.Prgnt, cs2m.AnxtyLH, margins = 1)
#----------------------

#Dealing with files
j = grades.sample(20)
j.head(3)
j.to_csv('./output/j.csv')
