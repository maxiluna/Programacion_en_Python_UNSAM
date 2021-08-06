# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:41:30 2021

@author: maximiliano.luna
"""


import csv
f = open('C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/missing.csv')
#f = open('C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
costototal = 0
for row in rows:
    try:
        costototal = costototal + (int(row[1]) * float(row[2]))
    except ValueError:
        print(f'Warning --> Continua')
print('Costo total: ', costototal)
