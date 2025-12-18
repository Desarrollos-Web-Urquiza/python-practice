def suma(**kwargs ):
    valor = kwargs.get('valor', 'No contiene el valor')
    print(valor)
    # * --> n valores --> tuplas
    # ** --> n valores --> diccionarios

    
    # resultado = 0
    # for valor in args:
    #     resultado = resultado + valor
    # return resultado
    # print(argumento)
    # print(type(argumento))

# def suma_tres(valor_uno, valor_dos, valor_tres):
#     return valor_uno + valor_dos + valor_tres

resultado = suma(valor = "eduardo", x = 2, y = 9, z = True)
print(resultado)