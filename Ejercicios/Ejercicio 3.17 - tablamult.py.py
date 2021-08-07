# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 08:16:29 2021

@author: maximiliano.luna
"""

def tabla_multiplicar():
    contador = 0
    headers = tuple([i for i in range(10) ])
    subrayado = ('-'*54)
    print('%9d%5d%5d%5d%5d%5d%5d%5d%5d%5d' % headers)
    print('%55s' % subrayado)

    for i in range(10):
        #Imprime valores por linea
        print(f'{i:>3d}:{contador:>5d}',end='')
        for _ in range(9):
            contador += i
            print(f'{contador:>5d}',end='')
        #Imprime el salto de linea
        print('')
        contador = 0

tabla_multiplicar()
