# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:12:16 2021

@author: maximiliano.luna
"""

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
    # agrego el elemento e al principio de la lista invertida
        i = len(lista)
        while i > 0:    # tomo el último elemento
            i = i-1
            invertida.append(lista.pop(i))  #
        return invertida

invertir_lista([1, 2, 3, 4, 5])
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
