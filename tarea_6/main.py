#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Convierte temperaturas en grados Fahrenheit entre el rango de 32 a 212, en grados Celcius,
ejemplificando el uso de excepciones si ocurre algún error

@author: Jesus Rivera
CDMX
"""


class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, temperatura):
        self.f = temperatura

    def __str__(self):
        return f'La temperatura {self.f}, no esta en el rango {self.min_f}, {self.max_f}.'
    

def fToc(f):
    if f < FahrenheitError.min_f or FahrenheitError.max_f<f:
        raise FahrenheitError(f)
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    fahrenheit = input('Ingrese la temperatura en grados Fahrenheit ')
    try:
        fahrenheit = float(fahrenheit)
    except ValueError as ex:
        print(ex)
    else:
        try:
            celcius = fToc(fahrenheit)
        except  FahrenheitError as ex:
            print(ex)
        else:
            print(f'la temperatura en celcius es: {celcius: .1f}')
