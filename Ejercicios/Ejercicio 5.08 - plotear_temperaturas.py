# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:17:45 2021

@author: maximiliano.luna
"""

import numpy as np
import matplotlib.pyplot as plt 

def histograma(ruta):
    temperaturas = np.load(ruta)
    plt.hist(temperaturas, bins=35)
    plt.show()

histograma('../Data/temperaturas.npy')
