# def palindromo():
#     nuevo_valor = frase.replace(" ", "")  #Variables Locales
#     print(frase)
#     return nuevo_valor == nuevo_valor[::-1]

# frase = "anita lava la tina"
# resultado = palindromo()

# print(frase)
# print(frase)
# print(resultado)

def valor_global():
    global variable_global
    variable_global = 'Cambiar valor' #Variable Local

def mostrar_global():
    print(variable_global)
    
def crear_global():
    global nueva_variable
    nueva_variable = 'Esto es una variable global'

crear_global()
print(nueva_variable)
# variable_global = 'Esto es una variable global'

# mostrar_global()
# valor_global()
# print(variable_global)