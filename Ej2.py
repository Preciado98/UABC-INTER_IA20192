#!/usr/bin/env python
# coding: utf-8

# # Ejercicio 2. Cálculo de raices
# 
# Utilizar las bibliotecas de numpy y matplotlib para resolver el siguiente problema propuesto.\n
# Realizar un programa que emplee la fórmula general para resolución de ecuaciones de segundo grado, de la forma:
# 
# $ ax^2 + bx + c $
# 
# Solicitar al usuario los valores para **a**, **b** y **c**, el programa debe mostrar la solución calculada. 
# Graficar la función con los parámetros
# capturados así como indicar con puntos las raíces calculadas, así como etiquetas en la
# gráfica mostrando el valor numérico de éstas.

# In[15]:


import numpy as np
import matplotlib.pyplot as plt


# In[16]:


print("Calculador de raices para ecuaciones de segundo grado\n")


# In[57]:


a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))


# In[61]:


d = (pow(b,2))-(4*a*c)
if d<0:
    print("Las raices son imaginarias")
else:
    def eq(x,a1,b1,c1):
        return ((a1*pow(x,2)) + (b1*x) + c1)
    x1 = ((-b) + np.sqrt(d))/(2*a)
    x2 = ((-b) - np.sqrt(d))/(2*a)
    x = np.linspace(-5, 5, 50)
    fig, bx = plt.subplots()
    bx.plot(x,eq(x,a,b,c), '--',label = 'funcion obtenida')
    bx.plot(x1,0,'*', label= 'x1')
    bx.plot(x2,0,'*', label= 'x2')
    bx.legend()
    plt.show()


# In[ ]:




