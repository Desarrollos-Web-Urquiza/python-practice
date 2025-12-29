class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email

    def __generar_password(self, password):
        return password.upper()

    # def get_password(self):
    #     return self.__password
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password = self.__generar_password(valor)


eduardo = Usuario('eduardo', 'eduardo123', 'eduardo@codigofacilito.com')
print(eduardo.password)
eduardo.password = 'Nuevo password'
print(eduardo.password)