class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email
    
    def __generar_password(self, password):
        return password.upper()
    
    def get_password(self): 
        return self.__password

eduardo = Usuario('eduardo', 'eduardo123', 'eduardo@codigofacilito.com')
print(eduardo.username)
# eduardo.__password = 'Aqui cambio todo el password'
# print(eduardo.password)
print(eduardo.email)     
print(eduardo.get_password())