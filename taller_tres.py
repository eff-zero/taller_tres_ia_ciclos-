#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 03:01:23 2021

@author: jesus
"""
# TALLER 3 - EJERCICIOS CON CICLOS - JESÚS H

# 1.
cantidad_carros = int(input('Ingrese el número de carros a entrar: '))


def conteo_calcomanias(cantidad_carros):
    color = {'amarillo': 0, 'rosa': 0, 'roja': 0, 'verde': 0, 'azul': 0}

    for carro in range(cantidad_carros):
        ultimo_digito = int(input('Ingrese el último dígito de su placa: '))
        if (ultimo_digito == (1 or 2)):
            color['amarillo'] = color['amarillo'] + 1
        elif (ultimo_digito == (3 or 4)):
            color['rosa'] = color['rosa'] + 1
        elif (ultimo_digito == (5 or 6)):
            color['roja'] = color['roja'] + 1
        elif (ultimo_digito == (7 or 8)):
            color['verde'] = color['verde'] + 1
        elif (ultimo_digito == (9 or 0)):
            color['azul'] = color['azul'] + 1
    return color


if (cantidad_carros > 0):
    conteo_calcomanias = conteo_calcomanias(cantidad_carros)
    for color, cantidad in conteo_calcomanias.items():
        print(f'El color {color} tiene {cantidad} carros')
else:
    print('Cantida invalida de carros. Debe ser mayor a 0')
