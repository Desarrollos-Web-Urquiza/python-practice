def decorador(is_valid = True): #A, B
    def _decorador(func): #A, B
        def before_action():
            print("Vamos a ejecutar la función")
        def after_action():
            print("Se ejecuto la función")
        def nueva_funcion(*args, **kwargs): #C
            if is_valid:
                before_action()
            resultado = func(*args, **kwargs)#La ejecuto
            after_action()
            #Agregue código
            return resultado

        return nueva_funcion #C
            
    return _decorador #A, B

@decorador()
def saluda():
    print("¡Hola mundo!")

#A, B, C son funciones
#A recibe como parametro B para poder crear C
@decorador()
def suma(num_uno, num_dos):
    return num_uno + num_dos

resultado = suma(80, 17)
print("El resultado de la suma es:", resultado)