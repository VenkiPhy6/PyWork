import pandas as pd
cs2m = pd.read_csv('./data/cs2m.csv')
#print(cs2m)
grades = pd.read_csv('./data/grades.csv')

#one sample
from scipy import stats
onesame = stats.ttest_1samp(a=cs2m.Age, popmean=40)
#print(onesame)

#paired 
pairedsam = stats.ttest_rel(grades.quiz1, grades.quiz2)
#print(pairedsam)

#Individual two sample
AnxtyL = cs2m[cs2m.AnxtyLH == 0]
#print(AnxtyL.shape)
AnxtyH = cs2m[cs2m.AnxtyLH == 1]
#print(AnxtyH.shape)
#print(stats.ttest_ind(AnxtyL.BP, AnxtyH.BP))

noPrgnt = cs2m[cs2m.Prgnt == 0]
yesPrgnt = cs2m[cs2m.Prgnt == 1]
#print(stats.ttest_ind(noPrgnt.BP, yesPrgnt.BP))

import numpy as np
print(pd.crosstab(cs2m.AnxtyLH, cs2m.DrugR, margins = True))
AnxtyDrugR = np.array([[11,5],[4,10]])
print(stats.chi2_contingency(AnxtyDrugR))