# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:00:18 2021

@author: maximiliano.luna
"""
import numpy as np

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=int)

def album_incompleto(album):
    return  len(album[album==0])==0

def comprar_figus(figus_total):
    return np.random.randint(0,figus_total)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cuenta_figus_compradas = 0
    while not album_incompleto(album):
        album[comprar_figus(figus_total)-1] += 1
        cuenta_figus_compradas+=1
    return cuenta_figus_compradas

def estimacion_figus(x_repeticiones, figus_total):
    lista_cuantas_figus = np.array([ cuantas_figus(figus_total) 
                                    for x in range(x_repeticiones) ])
    return np.ceil(lista_cuantas_figus.mean())

estimacion6 = estimacion_figus(x_repeticiones=1000, figus_total=6)
estimacion670 = estimacion_figus(x_repeticiones=100, figus_total=670)
print(f'Estimación para un album de 6 figus con 1000 repeticiones: \
      {estimacion6} figus fueron compradas')
print(f'Estimación para un album de 670 figus con 100 repeticiones: \
      {estimacion670} figus fueron compradas')
