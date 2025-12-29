class Lapiz: #Plantilla
    def __init__(self, color = 'Amarillo', contiene_borrador = False, usa_grafito = False):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito
    #Métodos
    def dibujar(self):
        print("El lapiz está dibujando")
    def borrar(self):
        if self.es_valido_para_borrar():
            print("El lapiz está borrando")
        else:
            print("No es posible borrar")
    def es_valido_para_borrar(self):
        return self.contiene_borrador

#Esto es un objeto
lapiz_generico = Lapiz()
lapiz_generico.dibujar()
lapiz_generico.borrar()
# its_valid_for_delete = lapiz_generico.es_valido_para_borrar()
# print(its_valid_for_delete)

