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


# 4.
num_hombres = int(input('Ingrese el número de hombres: '))
num_mujeres = int(input('Ingrese el número de mujeres: '))


def calcular_promedios(num_hombres, num_mujeres):
    promedio = {'hombres': 0, 'mujeres': 0, 'total': 0}
    sum_edades_hombres = 0
    sum_edades_mujeres = 0
    promedio_hombre = 0
    promedio_mujer = 0

    if (num_hombres != 0):
        for h in range(num_hombres):
            edad = int(input(f'Ingrese la edad del hombre #{h + 1}: '))
            sum_edades_hombres = sum_edades_hombres + edad
        promedio_hombre = sum_edades_hombres / num_hombres

    if (num_mujeres != 0):
        for m in range(num_mujeres):
            edad = int(input(f'Ingrese la edad de la mujer #{m + 1}: '))
            sum_edades_mujeres = sum_edades_mujeres + edad
        promedio_mujer = sum_edades_mujeres / num_mujeres  #

    if (num_mujeres != 0 or num_hombres != 0):
        sum_total_edades = sum_edades_hombres + sum_edades_mujeres
        num_total = num_hombres + num_mujeres
        promedio_total = sum_total_edades / num_total  #

    promedio['hombres'] = round(promedio_hombre)
    promedio['mujeres'] = round(promedio_mujer)
    promedio['total'] = round(promedio_total)

    return promedio


if (num_hombres >= 0 and num_mujeres >= 0):
    promedios = calcular_promedios(num_hombres, num_mujeres)
    print('')
    for sexo, promedio in promedios.items():
        print(f'Promedio {sexo} es de {promedio} años')
else:
    print('Número de hombres o mujeres invalido')


# 5.
cantidad_de_numeros = int(input('Ingrese la cantidad de números: '))


def numeros_en_set(cantidad_de_numeros):
    numeros = set()
    for n in range(cantidad_de_numeros):
        num = float(input(f'Ingrese su número #{n + 1}: '))
        numeros.add(num)
    return numeros


if (cantidad_de_numeros > 0):
    numeros = numeros_en_set(cantidad_de_numeros)
    menor = numeros.pop()
    for i in numeros:
        if (i < menor):
            menor = i
    print(f'\nEl número menos es {menor}')
else:
    print('Cantidad de números invalidos')


# 6.
def ingresar_ultimo_peso(num_miembros):
    ultimo_peso = []
    for m in range(num_miembros):
        peso = float(input(f'Digite el último peso del miembro {m + 1}: '))
        ultimo_peso.append(peso)
    return ultimo_peso


def calc_peso_actual(num_miembros, num_de_pesajes):
    peso_actual = []
    for m in range(num_miembros):
        acumulador_peso = 0
        for b in range(num_de_pesajes):
            peso = float(input(f'Peso mostrado en la báscula #{b+1} '
                               f'del miembro ({m + 1}): '))
            acumulador_peso = acumulador_peso + peso
        promedio_peso = acumulador_peso / num_de_pesajes
        peso_actual.append(promedio_peso)
        print('')
    return peso_actual


def diferencia_pesos(num_miembros=5, num_de_pesajes=10):
    ultimo_peso = ingresar_ultimo_peso(num_miembros)
    print('')
    peso_actual = calc_peso_actual(num_miembros, num_de_pesajes)
    diferencia_pesos = []

    for indice, promedio_peso in enumerate(peso_actual):
        dif_peso = promedio_peso - ultimo_peso[indice]
        diferencia_pesos.append(dif_peso)
    return diferencia_pesos


vector_diferencias = diferencia_pesos()
for indice, dif in enumerate(vector_diferencias):
    if (dif > 0):
        print(f'El miembro #{indice + 1} subió de peso')
    elif (dif == 0):
        print(f'El miembro #{indice + 1} tiene mismo peso')
    else:
        print(f'El miembro bajó #{indice + 1} de peso')


# 7.
def obtener_total_compra(seguir_agregando=True):
    indice = 1
    acumulador_gastos = 0
    while(seguir_agregando):
        valor_articulo = float(input(f'Valor del artículo #{indice}: '))
        cantidad_articulo = float(input(f'cantidad del artículo #{indice}: '))
        if (valor_articulo > 0 and cantidad_articulo > 0):
            gasto = valor_articulo * cantidad_articulo
            acumulador_gastos = acumulador_gastos + gasto
        else:
            print('\nCantidad o valor no valido')
            indice -= 1
        seguir_agregando = int(input('¿Desea seguir comprando?\n'
                                     '1. Sí\n'
                                     '0. No\n'
                                     '»» '))
        if (seguir_agregando):
            indice += 1
        else:
            return acumulador_gastos


gasto_total = obtener_total_compra()
print(f'\nEl gasto total de su compra debe ser de ${gasto_total:,}')


# 8.
precio_asiento = float(input('Ingrese el precio del los asientos: '))
cantidad_clientes = int(input('Ingrese el número de clientes: '))


def perdidas_por_categoria(precio_asiento, cantidad_clientes):
    categoria = {'5 a 14': [0, 0.35],
                 '15 a 19': [0, 0.25],
                 '20 a 45': [0, 0.10],
                 '46 a 65': [0, 0.25],
                 '66 ó más': [0, 0.35]
                 }
    # {[categoria]: [perdida, descuento%]}
    indice = 0
    while(cantidad_clientes != indice):
        edad = int(input(f'Por favor ingrese su edad ({indice + 1}): '))
        if (edad > 4 and edad < 15):
            descuento = precio_asiento * categoria['5 a 14'][1]
            categoria['5 a 14'][0] = categoria['5 a 14'][0] + descuento
        elif (edad > 14 and edad < 20):
            descuento = precio_asiento * categoria['15 a 19'][1]
            categoria['15 a 19'][0] = categoria['15 a 19'][0] + descuento
        elif (edad > 19 and edad < 46):
            descuento = precio_asiento * categoria['20 a 45'][1]
            categoria['20 a 45'][0] = categoria['20 a 45'][0] + descuento
        elif (edad > 45 and edad < 66):
            descuento = precio_asiento * categoria['46 a 65'][1]
            categoria['46 a 65'][0] = categoria['46 a 65'][0] + descuento
        elif (edad >= 66):
            descuento = precio_asiento * categoria['66 ó más'][1]
            categoria['66 ó más'][0] = categoria['66 ó más'][0] + descuento
        else:
            print('Edad no valida')
            indice -= 1
        indice += 1
    return categoria


if (precio_asiento > 0 and cantidad_clientes > 0):
    perdidas = perdidas_por_categoria(precio_asiento, cantidad_clientes)
    print('')
    for categoria, vector in perdidas.items():
        print(f'La categoria de {categoria} años perdió: ${vector[0]:,}')
else:
    print('Cantidad de asientos o clientes no valido')


# 9.
def calc_comision(cantidad_vendedores=2):
    total_comision_y_venta = []
    indice = 0
    while(cantidad_vendedores != indice):
        comision_y_venta = []  # [venta, comision]
        vendido = float(input(f'Valor vendido por empleado #{indice + 1}: '))
        if (vendido > 0 and vendido <= 20000000):  # 10%
            comision = vendido * 0.10
            comision_y_venta.append(vendido)   # [0] » [venta]
            comision_y_venta.append(comision)  # [0][1] » [venta, comision]
        elif (vendido > 20000000 and vendido < 40000000):  # 15%
            comision = vendido * 0.15
            comision_y_venta.append(vendido)
            comision_y_venta.append(comision)
        elif (vendido >= 40000000 and vendido < 80000000):  # 20%
            comision = vendido * 0.20
            comision_y_venta.append(vendido)
            comision_y_venta.append(comision)
        elif (vendido >= 80000000 and vendido < 160000000):  # 25%
            comision = vendido * 0.25
            comision_y_venta.append(vendido)
            comision_y_venta.append(comision)
        elif (vendido >= 160000000):  # 30%
            comision = vendido * 0.30
            comision_y_venta.append(vendido)
            comision_y_venta.append(comision)
        else:
            print('Valor de venta invalido')
            indice -= 1
        indice += 1
        total_comision_y_venta.append(comision_y_venta)
    return total_comision_y_venta


venta_y_comisiones = calc_comision()
print('')
for i, venta_comision in enumerate(venta_y_comisiones):
    print(f'Vendedor #{i+1}\n'
          f'Vendió: {venta_comision[0]:,}\n'
          f'Comisión: {venta_comision[1]:,}\n')


# 10.
def votacion(numero_votos=50000):
    votacion = [0, 0, 0]
    i = 0
    while (numero_votos != i):
        voto = int(input(f'¿Por cúal candidato desea votar? [Voto #{i+1}]\n'
                         '1. Candidato 1\n'
                         '2. Candidato 2\n'
                         '3. Candidato 3\n'
                         '»» '))
        if (voto == 1):
            votacion[0] = votacion[0] + 1
        elif (voto == 2):
            votacion[1] = votacion[1] + 1
        elif (voto == 3):
            votacion[2] = votacion[2] + 1
        else:
            print('Opción de voto no valida, elija entre 1, 2, ó 3')
            i -= 1
        i += 1
    return votacion


def voto_repetidos(votacion):
    votos_repetidos = []
    valor_repetido = 0
    for indice, votos in enumerate(votacion):
        if (votacion.count(votos) > 1):
            votos_repetidos.append(indice)
    if (votos_repetidos):
        valor_repetido = votacion[votos_repetidos[0]]
        return votos_repetidos, valor_repetido
    else:
        return votos_repetidos, valor_repetido


votacion = votacion()
votacion_mayor = max(votacion)
votos_repetidos, valor_repetido = voto_repetidos(votacion)
indice_voto_mayor = votacion.index(votacion_mayor)

print('')
for indice, votos in enumerate(votacion):
    print(f'El candidato #{indice + 1} obtuvo: {votos:,} voto(s)')

if (votos_repetidos):
    if (valor_repetido == votacion_mayor):
        print('')
        for candidatos in votos_repetidos:
            print(f'El candidato #{candidatos + 1} ha empatado '
                  f'con: {votacion_mayor:,} voto(s)')
    else:
        print(f'\nEl ganador es el candidato #{indice_voto_mayor + 1} '
              f'con: {votacion_mayor:,} voto(s)')
else:
    print(f'\nEl ganador es el candidato #{indice_voto_mayor + 1} '
          f'con: {votacion_mayor:,} voto(s)')
