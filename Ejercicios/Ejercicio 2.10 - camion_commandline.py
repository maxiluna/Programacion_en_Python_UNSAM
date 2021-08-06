# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:41:30 2021

@author: maximiliano.luna
"""


# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    costototal = 0
    for row in rows:
        try:
            costototal = costototal + (int(row[1]) * float(row[2]))
        except ValueError:
            print(f'Warning --> Continua')
    return costototal

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/camion.csv'
costo = costo_camion(nombre_archivo)
print('Costo total: ', costo)

