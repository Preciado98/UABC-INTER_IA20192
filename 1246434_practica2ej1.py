# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:28:50 2019

@author: preci
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

def gaus(m,s,x):
    return (1/(((2*mt.pi)*0.5))*s)*np.exp((-1/2)*pow((x-m)/s,2))

media = [0.5,1,1.5,2,0.5,1,1.5,2]
desv = [1,2,3,4,4,3,2,1]

j= len(media)
i=0

while i<=j:
    x = np.linspace(-10,10,200)
    fig, ax = plt.subplots()
    ax.plot(x,gaus(media[i],desv[i],x),'-')
    plt.show()
    i+=1
    if i==j:
        i+=1