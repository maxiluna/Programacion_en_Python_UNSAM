# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:23:14 2021

@author: maximiliano.luna
"""

def propagar(vector):
    listamodificada = vector
    propaga=0
    # Mientras el fuego se mantenga activo "True"
    while propagaresactivo(vector):
        propaga += 1
    # Una vez que el fuego sea "False" procede a devolver el listado
    return listamodificada

def propagaresactivo(vector):
    fuegoactivo = False
    longdevector = len(vector)
    for posdvector, valordvector in enumerate(vector):
        if valordvector==1 and posdvector<longdevector-1 and vector[posdvector+1]==0:
            vector[posdvector+1] = 1
            fuegoactivo = True
        if valordvector==1 and posdvector>0 and vector[posdvector-1]==0:
            vector[posdvector-1] = 1
            fuegoactivo = True
    return fuegoactivo

print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
#[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
print(propagar([ 0, 0, 0, 1, 0, 0]))
#[ 1, 1, 1, 1, 1, 1]
