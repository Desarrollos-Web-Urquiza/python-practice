class Usuario:
    def __new__(cls):
        print("Este método es el primero que se ejecuta")
        return super().__new__(cls)
    def __init__(self):
        print("Este método es el segundo que se ejecuta")
        # self.__password = "Este es un secreto"
    def __str__(self):
        return "Esto se imprime cuando intento mostrar el objeto"
    def __getattr__(self, nombre):
        print("Aqui mostramos que no se encontro el atributo")
        self.otros_metodos()
    def otros_metodos(self):
        print("Otro método")
    

    # def mostrar_password(self):
    #     print(self.__password)

# usuario = Usuario()
# usuario.__password  = "Este ya no es un secreto"
# print(usuario.__password)
# print(usuario.__dict__)
# usuario.mostrar_password()
# usuario.nombre = "Eduardo"
# print(usuario.nombre)
# print(usuario.__dict__)

usuario = Usuario()
print(usuario)

print(usuario.apellido)