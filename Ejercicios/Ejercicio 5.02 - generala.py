# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:22:01 2021

@author: maximiliano.luna

"""
import random
from pprint import pprint
from collections import Counter


def tiradados(dados = 5):
    dadostirada = [random.randint(1,6) for x in range(dados)]
    return dadostirada


def generala_no_servida():
    N = 100000
    cont = 0
    for x in range(N):
        dados = tiradados()
        repeticiones = Counter(dados)
        valor_max, veces_rep = repeticiones.most_common(1)[0]
        for y in range(2):
            dados = tiradados(5-veces_rep)
            repeticiones = Counter(dados)
            veces_rep += repeticiones[valor_max]
        if veces_rep == 5:
            cont+=1

    prob = cont/N
    print(f'Tire {N} veces, de las cuales {cont} saque generala.')
    print(f'Podemos estimar la probabilidad de sacar generala con {prob:.6f}.')

generala_no_servida()
