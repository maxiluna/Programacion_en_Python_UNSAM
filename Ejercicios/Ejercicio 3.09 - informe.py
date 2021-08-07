# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 08:26:59 2021

@author: maximiliano.luna
"""

from pprint import pprint

def leer_camion(path):
    camion = []
    with open(path,'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:
            camion.append((row[0], int(row[1]), float(row[2])))
    return camion

def leer_precios(path):
    precios = {}
    with open(path, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except:
            return precios
    return precios

with open('../Data/fecha_camion.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    select = ['nombre', 'cajones', 'precio']
    indices = [headers.index(ncolumna) for ncolumna in select]
#Ejercicio 3.9: La función zip()    
    row = next(rows)
    record = { ncolumna:row[index] for ncolumna, index in zip(select, indices)}
    print(record)
    camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]
    pprint(camion)
