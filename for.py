lista = (1,2,3,4,5,6,7,8,9,10,11,13,16)

for valor in lista:
    pass

nuevo_rango = range(0,20, 4)

for valor in nuevo_rango:
    pass

for indice, valor in enumerate(lista):
    print(valor, "tiene el indice", indice)

print(len(lista))

for valor in range(0, len(lista)):
    pass# print(valor)

for valor in 'Curso de Código Facilito':
    print(valor)

diccionario = { 'a': 10, 'b': 20, 'c': 500 }
for llave, valor in diccionario.items():
    print("la llave", llave, "tiene el valor de", valor)
