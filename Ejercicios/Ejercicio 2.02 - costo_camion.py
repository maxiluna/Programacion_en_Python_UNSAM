# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:41:30 2021

@author: maximiliano.luna
"""

#informe.py

#Ejercicio 2.18

import csv
...

# Trabajar_con_el_archivo_de_leer_camion

def leer_camion(nombre_archivo):
    camion= []
    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f)
        for row in rows:
            cajon = {}
            cajon["nombre"] = row[0]
            cajon["cajones"] = int(row[1])
            cajon ["precio"] = float(row[2])
            camion.append(cajon)
    return camion
camion = leer_camion (r"C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/camion.csv")


# Trabajar_con_el_archivo_de_leer_los_precios

def leer_precio(nombre_archivo):
    f = open (r"C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/precios.csv","rt") 
    rows = csv.reader (f) 
    
    precio = {}
    for row in rows:
        try:
            precio [row[0]]= float (row[1]) 
            
        except:
            pass
    return precio
precio= leer_precio (r"C:/Users/maximiliano.luna/Documents/Py/UNSAM/Clase02/Data/camion.csv")


# Calcular_el_costo_del_camion
costo = 0.0
venta = 0.0


for s in camion: 
    costo += s["cajones"] * s["precio"]
    venta += precio[s["nombre"]]*s["cajones"]
    
print ("El costo total del camion fue de:$",round(costo,2))
print ("la venta total del camion fue de:$",round(venta,2))

if venta > costo : 
    print ("Hubo ganancia de $",round(venta-costo,2))

elif venta == costo:
    print("No hubo ganancias ni pérdidas de $",round(venta-costo,2))
    
while venta < costo:
    print ("Hubo pérdidas de $", round(venta-costo,2))
