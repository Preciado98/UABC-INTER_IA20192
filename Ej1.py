#!/usr/bin/env python
# coding: utf-8

# # Ejercicio 1. Campanas de Gauss
# 
# Utilizar las bibliotecas de numpy y matplotlib para resolver el siguiente problema propuesto.
# Evaluar la siguiente función Gaussiana, en 50 puntos en un rango de $x$ en $[-10,10]$ para
# cada uno de los siguientes valores de **m** (media) y **s** (desviación)
# 
# $\LARGE f(x) = \frac{1}{\root{2\pi}s}exp(\frac{-1}{2}(\frac{x-m}{2})^2)$

# In[6]:


import numpy as np
import matplotlib.pyplot as plt


# In[18]:


s = [0.5,1,1.5,2,0.5,1,1.5,2]
m = [1,2,3,4,4,3,2,1]

def func(x,m,s):
    a = (1/(np.sqrt(2*np.pi)*s))
    b = np.exp((-1/2)*pow(((x-m)/s),2))
    return a*b


# In[27]:


x = np.linspace(-10,10,50)
fig, ax = plt.subplots()
ax.plot(x,func(x,m[0],s[0]), '-')
plt.show()

fig, ax = plt.subplots()
ax.plot(x,func(x,m[1],s[1]), '-')
plt.show()

fig, ax = plt.subplots()
ax.plot(x,func(x,m[2],s[2]), '-')
plt.show()
    
fig, ax = plt.subplots()
ax.plot(x,func(x,m[3],s[3]), '-')
plt.show()
    
fig, ax = plt.subplots()
ax.plot(x,func(x,m[4],s[4]), '-')
plt.show()
    
fig, ax = plt.subplots()
ax.plot(x,func(x,m[5],s[5]), '-')
plt.show()
    
fig, ax = plt.subplots()
ax.plot(x,func(x,m[6],s[6]), '-')
plt.show()
    
fig, ax = plt.subplots()
ax.plot(x,func(x,m[7],s[7]), '-')
plt.show()
    

