# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:41:30 2021

@author: maximiliano.luna
"""

# informe.py
import csv

def leer_precios(nombre_archivo):
    precios=[]
    diccionario={}
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)              
    try:
        for row in rows:
            diccionario = { row[0]: float(row[1])}
            precios.append(diccionario)
    except:
        pass
    return precios    


def leer_camion(nombre_archivo):
    camion=[]

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        cabecera = next(rows)
        for row in rows:
            diccionario={}
            diccionario[cabecera[0]] = row[0]
            diccionario[cabecera[1]] = int(row[1])
            diccionario[cabecera[2]] = float(row[2])
            camion.append(diccionario)
    return camion


def verificacamion(datosdecamion):
    totalporcamion = 0
    for x in datosdecamion:
        totalporfruta = x['cajones']*x['precio']
        totalporcamion += totalporfruta
    return totalporcamion


def recaudacion(pagado, ventas):
    totaldeventas = 0
    for x in pagado:
        for y in ventas:
            try:
                frutaventa = y[x['nombre']]
            except:
                pass
            totalporfruta = x['cajones']*frutaventa
        totaldeventas += totalporfruta
    return totaldeventas 


datosprecios = leer_precios('C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/precios.csv') 
#
datosdecamion = leer_camion('C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/camion.csv') 
#
costototalcamion = verificacamion(datosdecamion)
print(f'1 - Se le pago al productor un total de $ {costototalcamion} por la carga')
#
totaldeventas = recaudacion(datosdecamion, datosprecios)
print(f'2 - El valor total de venta por todo el camion fue de $ {totaldeventas}')
#¿Hubo ganancia o pérdida? El programa debe imprimir 
#por pantalla un balance con estos datos.
if costototalcamion < totaldeventas:
    ganancia = totaldeventas - costototalcamion
    print(f'Resultado: Hubo una ganancia de $ {ganancia:.2f}')
else:
    perdida = costototalcamion - totaldeventas
    print(f'Resultado: Hubo una perdida de $ {perdida:.2f}')