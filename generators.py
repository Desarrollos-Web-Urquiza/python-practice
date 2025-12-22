def generador(*args):
    for valor in args:
        yield valor * 10, True

for valor_uno, valor_dos in generador(1, 2, 3, 4, 5):
    print(valor_uno, valor_dos)