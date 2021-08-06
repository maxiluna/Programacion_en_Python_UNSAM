# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:41:30 2021

@author: maximiliano.luna
"""

def buscar_precio(fruta):
    f = open('C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/precios.csv', 'rt')
    archivo = f.read().splitlines()
    frutasexistes = []
    for x in archivo:
        lista = x.split(',')
        if fruta in lista and lista[0] == fruta:
            print(f'El precio de un cajón de {fruta} es: {lista[1]}')
            return lista[1]
    print(f'{fruta} no figura en el listado de precios')

buscar_precio('Frambuesa')
buscar_precio('Kale')
