# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:13:50 2021

@author: maximiliano.luna
"""


def buscar_u_elemento(lista, e):
    
    """
    En este primer ejercicio tenés que escribir una función 
    buscar_u_elemento() que reciba una lista y un elemento y 
    devuelva la posición de la última aparición de ese elemento 
    en la lista (o -1 si el elemento no pertenece a la lista).
    """
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
    return pos

buscar_u_elemento([1,2,3,2,3,4],1)
buscar_u_elemento([1,2,3,2,3,4],2)
buscar_u_elemento([1,2,3,2,3,4],3)
buscar_u_elemento([1,2,3,2,3,4],5)
