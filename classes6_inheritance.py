class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal): # Clase Padre
    @property
    def garras_retractiles(self):
        return True
    def cazar(self):
        print("El felino está cazando")

class Gato(Felino):
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino):
    pass

gato = Gato()
jaguar = Jaguar() 

print(gato.gato_cazador())
print(jaguar.garras_retractiles)
print("gato.terrestre", gato.terrestre)