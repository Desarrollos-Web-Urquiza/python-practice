# try:
#     print(2/0)
# except  ZeroDivisionError as ex:
#     print(ex)
#     print("No es posible dividir por 0") 

# print("Se termino el script")

# try:
#     lista = [1,2]
#     print(lista[9])
# except  IndexError as ex:
#     print(ex)
#     print("No es posible obtener el valor de 9") 
# except  ZeroDivisionError as ex:
#     print(ex)
#     print("No es posible dividir por 0") 

try:#Si o si
    lista = [1,2]
    print(lista[9])
except  Exception as ex:#Si cuando exista un error
    print(ex)
    print("No sé qué pasó, pero algo falló!") 
finally:#Si o Si
    print("Se terminó el script")
