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


# 2.
opcion_ani = int(input('Eliga el animal a estudiar [1, 2 ó 3]\n'
                       '1. Elefantes\n'
                       '2. Jirafas\n'
                       '3. Chimpancés\n'
                       '»» '))


def porcentajes(opcion_ani):
    cantidad_ani = {1: 20, 2: 15, 3: 40}
    nombre_ani = {1: 'Elefante', 2: 'Jirafa', 3: 'Chimpancé'}
    edad_ani = {'0 a 1 año': 0, '1 a 3 años': 0, 'mayor de 3 años': 0}

    for i in range(cantidad_ani[opcion_ani]):
        edad = int(input(f'Ingrese la edad del {nombre_ani[opcion_ani]} '
                         f'#{i + 1}: '))
        if (edad >= 0 and edad <= 1):
            edad_ani['0 a 1 año'] = edad_ani['0 a 1 año'] + 1
        elif (edad > 1 and edad < 3):
            edad_ani['1 a 3 años'] = edad_ani['1 a 3 años'] + 1
        else:
            edad_ani['mayor de 3 años'] = edad_ani['mayor de 3 años'] + 1

    for rango, valor in edad_ani.items():
        edad_ani[rango] = (valor * 100) / cantidad_ani[opcion_ani]
    return edad_ani, nombre_ani


if (opcion_ani > 0 and opcion_ani < 4):
    porcentajes, nombre_ani = porcentajes(opcion_ani)
    print('')
    for edad, porcentaje in porcentajes.items():
        print(f'El porcentaje de {nombre_ani[opcion_ani]}s de '
              f'{edad} de edad es de {porcentaje}%')
else:
    print('Opción de animal no valida')

# 3.
cantidad_obreros = int(input('Ingrese la cantidad de obreros laborando: '))


def salarios(cantidad_obreros):
    pago_normal = 20
    pago_extra = 25
    horas_normales = 40
    salarios = []

    for i in range(cantidad_obreros):
        horas = int(input(f'Número de horas del trabajador #{i + 1}: '))
        if (horas <= 40):
            salarios.append(horas * pago_normal)
        else:
            horas_extras = horas - horas_normales  # 51-40 = 11
            pago_extra = pago_extra * horas_extras  # 25*11 = 275
            pago_normal = pago_normal * horas_normales  # 20*40 = 800
            salarios.append(pago_normal + pago_extra)
    return salarios


if (cantidad_obreros > 0):
    salarios = salarios(cantidad_obreros)
    indice = 1
    print('')
    for salario in salarios:
        print(f'Al trabajador #{indice} le corresponden ${salario:,}')
        indice += 1
else:
    print('Cantidad de obreros invalida')
