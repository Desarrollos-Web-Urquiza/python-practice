class Circulo:
    
    _pi = 3.1416
    
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return self.radio * self.radio * self.pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

Circulo.pi = 20

print(Circulo.pi) #No necesito crear un objeto para que use PI

# print(circulo_uno.pi)
# print(circulo_dos.pi)

print(circulo_uno.area())
   