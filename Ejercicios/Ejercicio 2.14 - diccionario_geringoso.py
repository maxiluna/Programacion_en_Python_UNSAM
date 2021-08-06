# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:41:30 2021

@author: maximiliano.luna
"""

# geringoso.py
"""
Ejercicio 2.14: Diccionario geringoso.
Construí una función que, a partir de una lista de palabras, 
devuelva un diccionario geringoso. Las claves del diccionario
deben ser las palabras de la lista y los valores deben ser
sus traducciones al geringoso (como en el Ejercicio 1.18). 
Probá tu función para la lista ['banana', 'manzana', 'mandarina']. 
Guardá este ejercicio en un archivo diccionario_geringoso.py para 
entregar al final de la clase.
"""
def diccgeringoso(listadedatos):
    diccionario = {}
    for x in listadedatos:
        cadenafinal = ''
        for letra in x:
            if letra in 'aeiouáéíóú':
                cadenafinal += letra + 'p' + letra
            else:
                cadenafinal += letra
        diccionario[x]= cadenafinal
    print (diccionario)

lista = ['banana', 'manzana', 'mandarina']
diccgeringoso(lista)