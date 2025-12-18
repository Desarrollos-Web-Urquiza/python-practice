course = "Curso"

my_string = "Código Facilito!"

""" Formato """

result = '{a} de {b}'.format(a = course, b = my_string)
result = result.lower()
# result = result.upper()
# result = result.title()


""" Busqueda """
pos = result.find("código")
count = result.count("c")
# print(result[9])

new_string = result.replace("c", "x")
new_string = result.split(" ")

print(new_string)
