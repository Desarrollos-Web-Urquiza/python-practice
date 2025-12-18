diccionario = { 'a': True, 5: "esto es un string", 'a': 100, 'a': False } #Las claves deben ser inmutables

diccionario['c'] = "nuevo string" #creariamos clave/valor
diccionario['a'] = False #Si la llave/clave se encuentra actualiza si no crea

valor = diccionario['a'] #Obtenemos los valores
valor = diccionario.get('z', (12, 2)) 

# del diccionario[5]  #del nos ayuda a eliminar

# print(diccionario)
# print(valor)

llaves = tuple(diccionario.keys()) #objeto iterable
valores = tuple(diccionario.values())
diccionario_dos = { 'z': 23, 'w': 88 }

# diccionario['z'] = diccionario_dos['z']
# diccionario['w'] = diccionario_dos['w']

diccionario.update(diccionario_dos) #El que queremos que incremente

# print(llaves)
# print(valores)
print(diccionario)