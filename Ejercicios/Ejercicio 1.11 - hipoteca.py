# -*- coding: utf-8 -*-
"""
Created on Thu Mar  17 16:32:23 2021

@author: maximiliano.luna
"""

# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

pago_extra = 1000.00
mes = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
    if mes <= 12:
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        mes = mes +1
    elif mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        mes = mes +1
    elif saldo < pago_mensual:
        pago_mensual = saldo * (1+tasa/12)
        saldo = saldo * (1+tasa/12) - pago_mensual
    else:
        mes = mes +1
        saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    print('Total pagado hasta el momento: ', total_pagado, 'Saldo restante: ', saldo)

print('Total pagado', round(total_pagado, 2))
print('Meses: ', mes)
