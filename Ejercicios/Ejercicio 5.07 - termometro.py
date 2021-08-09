# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:01:32 2021

@author: maximiliano.luna
"""

import random
import numpy as np

def mediana(lista):
    lista = sorted(lista)
    largodelista = len(lista)
    if largodelista%2:
        mediana = lista[largodelista//2]
    else:
        mediana = (lista[largodelista//2 -1] + lista[largodelista//2])/2
    return mediana


def termometro(temp_medida, mu, sigma):
    temp_normalizadas = [ random.normalvariate(mu, sigma) 
                                 for i in range(999)]
    temp_simulada = [ temp_medida+temp 
                              for temp in temp_normalizadas]
    np.save('../Data/temperaturas', temp_simulada)
    print('Maximo: ', 
          round(max(temp_simulada),2))
    print('Minimo: ', 
          round(min(temp_simulada),2))
    print('Promedio: ', 
          round(sum(temp_simulada)/999 , 2))
    print('Mediana: ', 
          round(mediana(temp_simulada), 2))

termometro(37.5, 0, 0.2)
