vivo = True
class Personaje:
    
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre=nombre
        self.altura=altura
        self.velocidad=velocidad
        self.resistencia=resistencia
        self.fuerza=fuerza
        
    def correr(self):
        if vivo == True:
            distancia=1000
            tiempo = distancia / self.velocidad
            return tiempo
        else:
            print("El personaje esta muerto")
    def recuperarse(self):
        pass