# -*- coding: utf-8 -*-
"""
Created on Thu Mar  17 16:32:23 2021

@author: maximiliano.luna

Ejercicio 1.18: Geringoso rústico
Usá una iteración sobre el string cadena para agregar 
la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
"""
cadena = input('Ingrese una palabra a geringosear: ')
cadenalista = list(cadena)
cadenafinal = ''
for letra in cadenalista:
    if letra in 'aeiouáéíóú':
        cadenafinal += letra + 'p' + letra
    else:
        cadenafinal += letra
print(cadenafinal)
