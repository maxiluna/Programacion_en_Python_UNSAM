# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 09:01:54 2021

@author: maximiliano.luna
"""

import csv
from pprint import pprint
from collections import Counter

#Ejercicio 3.18: Lectura de los árboles de un parque
def leer_parque(path, parque):
    lista_parque = []
    with open(path, 'rt', encoding="utf8") as f:
        headers = next(f).split(',')
        rows = csv.reader(f)
        for row in rows:
            aux_dic = dict(zip(headers, row))
            if aux_dic['espacio_ve'] == parque:
                lista_parque.append(aux_dic)
    return lista_parque

def leer_arboles(path):
    with open(path,encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        conv = [{name: val for name, val in zip(headers,row)} for row in rows]
    return conv

#Ejercicio 3.19: Determinar las especies en un parque
def especies(lista_arboles):
    conjunto = []
    for arbol in lista_arboles:
        conjunto.append(arbol['nombre_com'])
    return set(conjunto)


def contar_ejemplares(lista_arboles):
    existencia = Counter()
    for arbol in lista_arboles:
        existencia[arbol['nombre_com']] += 1
    return existencia.most_common(5)


def obtener_alturas(lista_arboles, especie):
    altura_lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            altura_lista.append(float(arbol['altura_tot']))
    return(altura_lista)


def maximo(lista):
    try:
        max_lista = float(lista[0])
        for i in range(1,len(lista)):
            if max_lista < float(lista[i]):
                max_lista = float(lista[i])
        return max_lista
    except:
        print("error al calcular el maximo de una lista, esta vacia o no se paso parametro")


def promedio(lista):
    try:
        acumulador = 0
        for altura in lista:
            acumulador += float(altura)
        return round(acumulador/len(lista), 2)
    except:
        print("error al calcular el maximo de una lista, esta vacia o no se paso parametro")


def obtener_inclinaciones(lista_arboles, especie):
    inclinacion = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinacion.append(arbol['inclinacio'])
    return inclinacion


def especimen_mas_inclinado(lista_arboles):
    especies_arboles_parque = list(especies(lista_arboles))
    inclinacion_maxima = maximo(obtener_inclinaciones(lista_arboles,especies_arboles_parque[0]))
    especie_maxima = especies_arboles_parque[0]

    for especie in especies_arboles_parque:
        if inclinacion_maxima < maximo(obtener_inclinaciones(lista_arboles,especie)):
            especie_maxima = especie
            inclinacion_maxima = maximo(obtener_inclinaciones(lista_arboles,especie))
    print(f'Especie: {especie_maxima}\t maxima inclinacion: {inclinacion_maxima}')


def especie_promedio_mas_inclinada(lista_arboles):
    especies_arboles_parque = list(especies(lista_arboles))
    inclinacion_promedio_maxima = promedio(obtener_inclinaciones(lista_arboles,especies_arboles_parque[0]))
    especie_maxima = especies_arboles_parque[0]

    for especie in especies_arboles_parque:
        if inclinacion_promedio_maxima < promedio(obtener_inclinaciones(lista_arboles,especie)):
            especie_maxima = especie
            inclinacion_promedio_maxima = promedio(obtener_inclinaciones(lista_arboles,especie))
    print(f'Especie: {especie_maxima}\t maxima inclinacion promedio: {inclinacion_promedio_maxima}')


print('\nEjercicio 3.20: Contar ejemplares por especie')                
for parque in ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']:
    print(f'\n  Parque: {parque}')
    pprint(contar_ejemplares(leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)))

print('\nEjercicio 3.21: Alturas de una especie en una lista')                
for parque in ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']:
    print(f'\n  Parque: {parque}')
    lista_arboles = obtener_alturas(leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque), 'Jacarandá')
    print('    Maximo: ',maximo(lista_arboles))
    print('    Promedio: ',promedio(lista_arboles))

print('\nEjercicio 3.22: Inclinaciones por especie de una lista')
print(obtener_inclinaciones(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'), 'Jacarandá'))
print('\nEjercicio 3.23: Especie con el ejemplar más inclinado')
especimen_mas_inclinado(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO'))
print('\nEjercicio 3.24: Especie más inclinada en promedio') 
especie_promedio_mas_inclinada(leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS'))
