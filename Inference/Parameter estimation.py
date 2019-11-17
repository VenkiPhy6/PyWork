
# coding: utf-8

# # Poisson Distribution for D=1.7

# In[2]:


from numpy import*
import matplotlib.pyplot as plt
from scipy.special import factorial
N=arange(0,10,1)
D=1.7
Pdf=(D**N/factorial(N))* exp(-D)
plt.bar(N, Pdf, facecolor='orange', alpha=0.95, ec='brown')
plt.xlabel("Number of counts N",fontsize=16)
plt.ylabel("prob(N|D=1.7)",fontsize=16)
plt.show()


# # Poisson Distribution for D=12.5

# In[2]:


from numpy import*
import matplotlib.pyplot as plt
from scipy.special import factorial
N=arange(0,24,2)
D=12.5
Pdf=(D**N/factorial(N))* exp(-D)
plt.bar(N, Pdf, facecolor='blue', alpha=0.55, ec='brown')
plt.xlabel("Number of counts N",fontsize=16)
plt.ylabel("prob(N|D=12.5)",fontsize=16)
plt.show()


# # Redshift problem

# In[3]:


from numpy import*
import matplotlib.pyplot as plt
x =loadtxt('counting_data.dat')
entries=plt.hist(x, bins='auto', histtype='step', alpha=1, ec='black')
hist, bins=histogram(x, bins='auto')
plt.xlabel("Measurement variable x",fontsize=16)
plt.ylabel("Number of counts N",fontsize=16)
plt.title('Histogram', fontsize=16)
print('H=', hist)
print('B=', bins)


# # Contour Plot

# In[33]:


from numpy import*
import matplotlib.pyplot as plt
from scipy.misc import factorial
n0=20
x0=5
w=2
N= array([124,137,212,327,
     325,217,134,125,
     125,126,123,124,
     126,123,128,124])
x = array([0.00657351432,1.25249168 ,2.49840985, 3.74432802
 ,4.99024619 ,6.23616436 ,7.48208253 ,8.72800070
 ,9.97391886 ,11.2198370 ,12.4657552, 13.7116734
 ,14.9575915, 16.2035097, 17.4494279 ,18.6953460])
width = x[2]-x[1]
A=linspace(1,50,50)
B=linspace(1,50,50)
# D=zeros((50,50,16), dtype=float)
R=zeros((50,50), dtype=float)
L=zeros((50,50), dtype=float)
# constant=log(n0)
for m in range(len(A)):
    for p in range(len(B)):
        D= (n0*(((A[m]*(exp((-(x-x0))**2/((w)**2)))+B[p]))))*(width)
        R[m,p]= sum((N*log(D))-D)
        print(R)

L = R

amp, bckgnd= meshgrid(A, B)
cp = plt.contourf(amp, bckgnd, exp(L))
# plt.clabel(cp, inline=True, 
#           fontsize=10)
# plt.colorbar(cp)
plt.xlabel("A",fontsize=16)
plt.ylabel("B",fontsize=16)
plt.title('A Vs B')
plt.show()


# In[148]:


from numpy import*
import matplotlib.pyplot as plt
from scipy.misc import factorial
n0=20
x0=5
w=2

# def get_Dk (A,B,x):
#     ----
#     -----
#     return 

# def logL (Nk,A,B,x):
#     Dk = get_Dk()
#     ---
#     --
    
#     return logl

N= array([124,137,212,327,
     325,217,134,125,
     125,126,123,124,
     126,123,128,124])
x = array([0.00657351432,1.25249168 ,2.49840985, 3.74432802
 ,4.99024619 ,6.23616436 ,7.48208253 ,8.72800070
 ,9.97391886 ,11.2198370 ,12.4657552, 13.7116734
 ,14.9575915, 16.2035097, 17.4494279 ,18.6953460])
width = x[2]-x[1]
A=linspace(1,50,50)
B=linspace(1,50,50)
# D=zeros((50,50), dtype=float)
# R=zeros((50,50), dtype=float)
L=zeros((50,50), dtype=float)
# constant=log(n0)
for m in range(len(A)):
    for p in range(len(B)):
        D=(n0*(((A[m]*(exp((-(x-x0))**2/((w)**2)))+B[p]))))*(width)
        L[m,p]= sum((N*log(D))-D)
        print(L)
#         ind = unravel_index(argmax(L, axis=None), L.shape)
#         print(ind)
#         print(L)
print(max(L.flatten()))

# L_max=max(L.flatten())

# print(L_max)
# print(ind)
# result=where(L==amax(L))
# print(result)
# listOfCordinates = list(zip(result[0], result[1]))

# print(listOfCordinates)
# L_max=max(L.flatten())
# print(shape(L))
# print('Maximum value of L', L_max)
# L_NEW=L/L_max
# # print(L_NEW)
# print(exp(L)-exp(L_NEW))

# L_max=max(L.flatten()L
# print(L_max)
# Norm_L=L/L_max
# print(Norm_L)

# print(exp(L_max))
# print(exp(L)/exp(L_max))
# L_

# R=exp(L/L_max)

# amp, bckgnd= meshgrid(A, B)
# cp = plt.contourf(amp, bckgnd,R)
# plt.clabel(cp, inline=True, 
#           fontsize=10)
# plt.colorbar(cp)
# plt.xlabel("A",fontsize=16)
# plt.ylabel("B",fontsize=16)
# plt.title('A Vs B')
# plt.show()


# In[93]:


max(L.flatten())


# In[159]:


from numpy import*
import matplotlib.pyplot as plt
from scipy.misc import factorial
n0=20
x0=5
w=2

def get_Dk(A,B,x,width):
    A=arange(1,51,1)
    B=arange(1,51,1)
    x=array([0.00657351432,1.25249168 ,2.49840985, 3.74432802
         ,4.99024619 ,6.23616436 ,7.48208253 ,8.72800070
         ,9.97391886 ,11.2198370 ,12.4657552, 13.7116734
         ,14.9575915, 16.2035097, 17.4494279 ,18.6953460])
    width = x[2]-x[1]
    return (n0*(((A*(exp((-(x-x0))**2/((w)**2)))+B))))*(width)


def logL(A,B,N,D,x):
    D=get_Dk(A,B,x,width)
    N= array([124,137,212,327,
              325,217,134,125,
              125,126,123,124,
              126,123,128,124])
    print(sum((N*log(D))-D))
    

    
       
        

    
 
   


   
    
            


   





        

# amp, bckgnd= meshgrid(A, B)
# cp = plt.contourf(amp, bckgnd, exp(L))
# # plt.clabel(cp, inline=True, 
# #           fontsize=10)
# plt.colorbar(cp)
# # plt.xlabel("A",fontsize=16)
# # plt.ylabel("B",fontsize=16)whats
# # plt.title('A Vs B')
# plt.show()


# In[155]:


from numpy import*
import matplotlib.pyplot as plt
from scipy.misc import factorial
n0=20
x0=5
w=2


N= array([124,137,212,327,
         325,217,134,125,
        125,126,123,124,
         126,123,128,124])
x = array([0.00657351432,1.25249168 ,2.49840985, 3.74432802
 ,4.99024619 ,6.23616436 ,7.48208253 ,8.72800070
 ,9.97391886 ,11.2198370 ,12.4657552, 13.7116734
 ,14.9575915, 16.2035097, 17.4494279 ,18.6953460])
width = x[2]-x[1]
A=linspace(1,50,50)
B=linspace(1,50,50)
#D=zeros((50,50), dtype=float)
# R=zeros((50,50), dtype=float)
L=zeros((50,50), dtype=float)
for m in range(len(A)):
    for p in range(len(B)):
        D= (n0*(((A[m]*(exp((-(x-x0))**2/((w)**2)))+B[p]))))*(width)
        L[m,p]= sum((N*log(D))-D)
#         print(L)
L_max=max(L.flatten())
print(L_max)
print(exp(L))
# exp(L)=exp(L)/max(exp(L))

# ind = unravel_index(argmax(L, axis=None), L.shape)
# print(ind)
amp, bckgnd= meshgrid(A, B)
cp = plt.contourf(amp, bckgnd, exp(L))
plt.clabel(cp, inline=True, 
          fontsize=10)
plt.colorbar(cp)
plt.xlabel("A",fontsize=16)
plt.ylabel("B",fontsize=16)
plt.title('A Vs B')
plt.show()


# In[186]:


from numpy import*
import matplotlib.pyplot as plt
x0=5
n0=20
w=2
B=2
A=5
x = array([0.00657351432,1.25249168 ,2.49840985, 3.74432802
 ,4.99024619 ,6.23616436 ,7.48208253 ,8.72800070
 ,9.97391886 ,11.2198370 ,12.4657552, 13.7116734
 ,14.9575915, 16.2035097, 17.4494279 ,18.6953460])
D=n0*[A*exp(-(x-x0)**2/ w**2) + B]
print(D)
plt.plot(x,D,markersize=1.5)
plt.show()


# In[ ]:


from numpy import*
import matplotlib.pyplot as plt
from scipy.misc import factorial
n0=20
x0=5
w=2
N= array([124,137,212,327,
     325,217,134,125,
     125,126,123,124,
     126,123,128,124])
x = array([0.00657351432,1.25249168 ,2.49840985, 3.74432802,4.99024619 ,6.23616436 ,7.48208253 ,8.72800070,9.97391886 ,11.2198370 ,12.4657552, 13.7116734,14.9575915, 16.2035097, 17.4494279 ,18.6953460])
width = x[2]-x[1]
A=linspace(1,50,50)
B=linspace(1,50,50)
L=zeros((50,50), dtype=float)
for m in range(len(A)):
    for p in range(len(B)):
        D=(n0*(((A[m]*(exp((-(x-x0))**2/((w)**2)))+B[p]))))*(width)
        L[m,p]= sum((N*log(D))-D)
        print(L)
#         ind = unravel_index(argmax(L, axis=None), L.shape)
#         print(ind)
#         print(L)
print(max(L.flatten()))

# L_max=max(L.flatten())

# print(L_max)
# print(ind)
# result=where(L==amax(L))
# print(result)
# listOfCordinates = list(zip(result[0], result[1]))

# print(listOfCordinates)
# L_max=max(L.flatten())
# print(shape(L))
# print('Maximum value of L', L_max)
# L_NEW=L/L_max
# # print(L_NEW)
# print(exp(L)-exp(L_NEW))

# L_max=max(L.flatten()L
# print(L_max)
# Norm_L=L/L_max
# print(Norm_L)

# print(exp(L_max))
# print(exp(L)/exp(L_max))
# L_

# R=exp(L/L_max)

# amp, bckgnd= meshgrid(A, B)
# cp = plt.contourf(amp, bckgnd,R)
# plt.clabel(cp, inline=True, 
#           fontsize=10)
# plt.colorbar(cp)
# plt.xlabel("A",fontsize=16)
# plt.ylabel("B",fontsize=16)
# plt.title('A Vs B')
# plt.show()

