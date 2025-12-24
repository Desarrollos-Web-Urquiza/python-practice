class Lapiz: #Plantilla
    color = 'Amarillo' #Atributos
    contiene_borrador = False
    usa_grafito = True 
    #Métodos
    def dibujar(self):
        print("El lapiz está dibujando")
    def borrar(self):
        print("El lapiz está borrando")
    def es_valido_para_borrar(self):
        return self.contiene_borrador

#Esto es un objeto
lapiz_generico = Lapiz()
lapiz_generico.dibujar()
lapiz_generico.borrar()
its_valid_for_delete = lapiz_generico.es_valido_para_borrar()
print(its_valid_for_delete)

