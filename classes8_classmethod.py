class Animal:
    valador = True

class Cocodrilo(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def new(cls, nombre):
        cls.valador = False
        return Cocodrilo(nombre)
    
cocodrilo = Cocodrilo.new('coco')
print(cocodrilo.nombre)
print(cocodrilo.valador)