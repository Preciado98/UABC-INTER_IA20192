# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:37:15 2019

@author: preci
"""
import numpy as np
import matplotlib.pyplot as plt

def chicharronera(a,b,c,opc):
    if opc==1:
        return (-b+((b*b - (4*a*c))*0.50))/(2*a)
    else:
        return (-b-((b*b - (4*a*c))*0.5))/(2*a)

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))


aux = pow(b,2)-(4*a*c)

if aux>0:
    x = np.linspace(-5,5,10)
    y0 = a*pow(x,2) + b*x +c

    r1 = chicharronera(a,b,c,1)
    r2 = chicharronera(a,b,c,0)

    fig, ax = plt.subplots()
    ax.plot(x,y0,'--',label='ax^2 +bx +c')
    ax.plot(r1,0,'*', label= 'x1')
    ax.plot(r2,0,'*', label= 'x2')
    ax.legend()
    plt.show()
else:
    print("Raices no reales")



