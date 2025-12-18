# lista = [] #false

# for valor in range(0, 101):
#     lista.append(valor)

lista = [ valor for valor in range(0, 101) if valor % 2 == 0 ]

#1 - Valor a agregar a la lista
#2 - Un ciclo, por ejemplo "for"

tupla = tuple( ( valor for valor in range(0, 101) if valor % 2 != 0 ) )

diccionario = { indice: valor for indice, valor in enumerate(lista) if indice < 10 }

print(lista)
print(tupla)
print(diccionario)