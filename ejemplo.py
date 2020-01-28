# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:07:43 2019

@author: preci
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

def dif(x,h,func):
    return (func(x+h) -func(x-h))/(2*h)

#funcion en e^x

x = np.linspace(-5,5,50)
y1 = np.exp(x)
y2= dif(x,0.01,np.exp)

fig, ax = plt.subplots()
ax.plot(x,y1,'--',label='exp')
ax.plot(x,y2,'--',label='def')
ax.legend()
plt.show()

#funcion en e^-2*x**2

j = np.linspace(-5,5,50)
k1 = np.exp(-2*(x**2))
k2= dif(j,0.01,np.exp)

fig, ax = plt.subplots()
ax.plot(j,k1,'--',label='exp')
ax.plot(j,k2,'--',label='def')
ax.legend()
plt.show()


#funcion en cos(x)

j = np.linspace(-2*mt.pi,2*mt.pi,50)
k1 = np.cos(j)
k2= dif(j,0.01,np.cos)

fig, ax = plt.subplots()
ax.plot(j,k1,'--',label='exp')
ax.plot(j,k2,'--',label='def')
ax.legend()
plt.show()


#funcion en ln(x)

j = np.linspace(1,10,50)
k1 = np.log(j)
k2= dif(j,0.01,np.cos)

fig, ax = plt.subplots()
ax.plot(j,k1,'--',label='exp')
ax.plot(j,k2,'--',label='def')
ax.legend()
plt.show()
