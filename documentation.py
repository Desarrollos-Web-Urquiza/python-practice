def generador(*args):
    """Recibe n cantidad de números y regresa el número además de regresar\n True o False si el número es mayor a 5
    """
    for valor in args:
        yield valor * 10, True

# nombre = generador.__name__

# documentacion = generador.__doc__
# print(nombre, " : ")
# print(documentacion)