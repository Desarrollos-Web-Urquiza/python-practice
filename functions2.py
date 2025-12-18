def suma( valor_uno, valor_dos, valor_tres ):
    return valor_uno + valor_dos + valor_tres

def division( valor_uno, valor_dos ):
    return valor_uno / valor_dos

def multiplicacion( valor_uno, valor_dos = 10):
    return valor_uno * valor_dos

def multiples_valores():
    return "String", 1, True, 25.6

# resultado = division( valor_dos = 10, valor_uno = 100 )  #Primera
# resultado = division( 100, 10 ) #Segunda
resultado = multiples_valores() #Primera

# string, entero, booleano, float = multiples_valores() #Segunda

# string = resultado[0]
# entero = resultado[1]
# booleano = resultado[2]
# float = resultado[3]    

# print( string )
# print( entero )
# print( booleano )
# print( float )

def mostrar_resultado( funcion ):
    print(funcion(6, 8))

mi_variable =  multiplicacion
# resultado = mi_variable(6, 8) 
# print( resultado )

mostrar_resultado( mi_variable )

