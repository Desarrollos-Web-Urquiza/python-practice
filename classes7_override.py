class Animal:
    pass

class Felino(Animal): 
    pass
   
class Mascota:
    nombre = ''

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

class Gato(Felino, Mascota):
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.nombre_gato = nombre

    def gato_cazador(self):
        self.cazar()

    def mostrar_nombre(self):  #    Sobreescritura de métodos
        Mascota.mostrar_nombre(self)
        print("El nombre de gato es: {}".format(self.nombre))

gato = Gato('Patricio')
# gato.nombre = 'Patricio'
gato.mostrar_nombre()