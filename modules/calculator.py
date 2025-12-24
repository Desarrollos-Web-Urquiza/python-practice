# !/usr/bin/python3

"""
    Aquí colcamos todo lo que hace el modulo a que contexto le corresponde
"""

__author__ = "Eduardo Ismael García Pérez"
__copyright__ = "Copyright 2016, Código facilito"
__credits__ = "Código facilito"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Eduardo Ismael"
__email__ = "eduardo@codigofacilito.com"
__status__ = "Developer"

def suma(num_uno, num_dos):
    """
    Regresa un número entero el cual es el resultado de una suma
    """
    return num_uno + num_dos


def resta(num_uno, num_dos):
    """
    Regresa un número entero el cual es el resultado de una resta
    """
    return num_uno - num_dos


def multiplicacion(num_uno, num_dos):
    """
    Regresa un número entero el cual es el resultado de una multiplicación
    """
    return num_uno * num_dos


def division(num_uno, num_dos):
    """
    Regresa un número real el cual es el resultado de una división
    """
    return num_uno / num_dos

def saluda():
    print("Saluda")
# print(__name__)
if __name__ == '__main__':
    saluda()