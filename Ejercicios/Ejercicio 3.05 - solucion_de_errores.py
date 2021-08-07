# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:50:01 2021

@author: maximiliano.luna
"""

#solucion_de_errores.py
"""
¿Qué tipo de errores tiene cada uno?

En el archivo solucion_de_errores.py separá las correcciones 
de los distintos códigos con una línea que contenga solamente 
los símbolos #%% seguido de una o varias líneas comentadas 
indicando el ejercicio y el problema que tenía.
"""
#Ejercicio 3.1. Función tiene_a()
# Pregunta: ¿Anda bien en todos los casos de prueba?
# Comentario: El error era que luego del primer ingreso al while
#       siempre sale del mismo por la función 'return'.
# Lo corregí incorporando la suma para i durante el while
# sobre el else y quitando el return False para incorporarlo
# en la salida del while, solo funcionando si nunca cumplió la
# validación.
# A continuación va el código corregido


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or 'A':
            return True
        else:
            i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#Ejercicio 3.2. Función tiene_a(), nuevamente
# Pregunta: ¿Anda bien en todos los casos de prueba?
# Comentario: No, hasta corregir los errore de sintaxis.
# Le corregí; 1 - incorporando dos puntos al final de la funcion, del while y del if
#  2 - Incorporando la equivalencia de valor con doble == igual.
#  3 - Modifque el return Falso por False.
# A continuación va el código corregido


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#Ejercicio 3.3. Función tiene_uno()
# Pregunta: ¿Anda bien en todos los casos de prueba?
# Comentario: No, el argumento de la ultima llamada "1984" no cumple con la funcion len
#       por no ser un (string, tupla, lista o diccionario).
# Le corregí llamadando a la funcion con el numero asignando como string.
# A continuación va el código corregido


def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(str(1984)))


#Ejercicio 3.4. Función tiene_uno()
#Pregunta: La siguiente suma no da lo que debería:
# Comentario: No, la funcion no tiene un return que informe el resultado de c.
# Le corregí incorporando a la salida de la funcion "return c".
# A continuación va el código corregido


def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#Ejercicio 3.5. Función tiene_uno()
#Pregunta: El siguiente ejemplo usa el dataset de la clase anterior, 
#       pero no lo imprime como corresponde, ¿podés determinar por qué y 
#   explicarlo brevemente en la versión corregida?
# Comentario: En cada append guarda el ultimo valor recolectado y 
#   lo asigna en todas las posiciones incluidas en la lista camion.
#   Lo resolvi incorporando los valores en llave, asignando el valor a cada clave.
# A continuación va el código corregido


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {encabezado[0]:fila[0],
                    encabezado[1]:int(fila[1]),
                    encabezado[2]:float(fila[2])}
            camion.append(registro)
        return camion

camion = leer_camion('C:/Users/maximiliano.luna/Documents/Py/UNSAM/Data/camion.csv')
pprint(camion)
