def factorial_numero(numero = 5):
    factorial = 1
    while numero > 1:
        factorial = factorial * numero
        numero -= 1
    return factorial

resultado = factorial_numero(5)
print(resultado)

resultado = factorial_numero(4)
print(resultado)

resultado = factorial_numero(6)
print(resultado)
