def crear_funcion(num_uno, num_dos):#Closure
    def validacion():
        print('Se ejecuta validacion')
        return num_uno > 0 and num_dos > 0 
    return validacion


def aplica_funcion(func):
    resultado = func()
    print(resultado)

nueva_funcion = crear_funcion(10, 5)
aplica_funcion(nueva_funcion)