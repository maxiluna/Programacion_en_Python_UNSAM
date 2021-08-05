# -*- coding: utf-8 -*-
"""
Created on Thu Mar  17 16:32:23 2021

@author: maximiliano.luna

Una pelota de goma es arrojada desde una altura de 100 metros y 
cada vez que toca el piso salta 3/5 de la altura desde la que cayó.

Escribí un programa rebotes.py que imprima una tabla mostrando las
alturas que alcanza en cada uno de sus primeros diez rebotes.
Tu programa debería generar una tabla que se parezca a esta:

"""
alturaarrojada = 100
cantidadrebotes = 10
saltadelpiso = 3/5

while cantidadrebotes > 0:
    alturaarrojada = alturaarrojada * saltadelpiso
    print(round(alturaarrojada, 4))
    cantidadrebotes = cantidadrebotes - 1
