"""
Created on Mon Dec 16 12:45:40 2019

@author: preci
"""

"""
Escribid una función en Python que, dada una lista de números, 
devuelva otra lista en orden inverso. Para realizar este ejercicio
 se deberá utilizar un bucle o estructura repetitiva.
No se permite el uso de funciones miembro de la clase
 list (en especial list.reverse()).
"""

"modo 1:"
def invierte(lista):
    return lista[::-1]

ejemplo = [1,2,3,4]

print(invierte(ejemplo))
"""Modo2:
    
    print(ejemplo[::-1])"""

"""
2. Escribid una función que, dado un número entero N, devuelva una lista con todos los
números primos hasta N. Para solucionar el ejercicio debéis crear una función auxiliar que
indique si un determinado número es primo (retornando un valor booleano).
"""
"""
def primos(n, lista):
    cont = 0
    i = 0
    while cont < n:
        i += 1
        if auxiliar(i):
            cont += 1
            lista.append(i)

def auxiliar(aux):
    num = 0
    if aux<2:
        return False
    
    for num in (2,aux):
        if aux%num==0:
            return False
        
    return True
    

lista=[]
numero= 17
print(primos(17,lista))
"""

"""

3. Escribid una función que reciba una tupla compuesta por caracteres, 
y devuelva una lista con los caracteres en mayúsculas. 
Debéis recorrer la tupla carácter a carácter para realizar
la conversión. Para convertir un carácter a mayúscula podéis 
usar el método upper(). Por ejemplo ’a’.upper() nos devuelve ’A’
."""


def mayusculas(string):
    lista = []
    
    ax = list(string)
    for i in ax:
        lista+=i.upper()
        
    return lista

cad = ("alejandra")
print(mayusculas(cad))

"""
4. Convertid el texto ’ejemplo’ en una lista que contenga sus 7 caracteres. 
Después convertidlo en una tupla y usando la función del ejercicio anterior 
obtened una lista con el texto en mayúsculas.
"""
c =[]
for i in "ejemplo":
    c+=i.upper()
    
print(c)
tupla = tuple(c)
print(tupla)

print(mayusculas(c))


"""

5. Escribid una función que, dada una lista de números, devuelva una lista 
con sólo los elementos en posición par.

def numpar(lista):
    al=[]
    for j in lista:
        if j%2==0:
         print(j)
            al+=j
    return al
            
    
lisnum = [1,2,3,4,5,6,7,8,9,0]
print(numpar(lisnum))
"""
"""
6. Extended la función anterior para que, dada una lista y unos índices, 
nos devuelva la lista resultado de coger sólo los elementos indicados por 
los índices. Por ejemplo si tenemos la lista [1,2,3,4,5,6] y los índices 
[0,1,3] debería devolver la lista [1,2,4].
"""
def indices(lista,cad):
    temp=[]
    
    for i in cad:
        for j in lista:
            temp+=lista[i]
    return temp

lisnum = [1,2,3,4,5,6,7,8,9,0]
indices = [0,3,4,6]
print(indices(lisnum,indices))