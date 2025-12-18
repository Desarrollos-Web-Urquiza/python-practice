# def suma(valor_uno, valor_dos):
#     return valor_uno + valor_dos 

mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos

formato = lambda sentencia : '¿{}?'.format(sentencia)
no_valor = lambda : 10
no_resultado = lambda : print('Debe de ejecutar una acción')
# resultado = formato('Puedes hacer esto una pregunta')
resultado = no_resultado()
print(resultado)