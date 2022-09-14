# Integrante: Boriani Juan Cruz

# Clase 1---------

class Vehiculos:
    def __init__(self,tipo,marca,modelo):
        velocidad=0
        self.tipo=tipo
        self.marca=marca
        self.modelo=modelo
    
    def caracteristicas(self):
        print(f"El vehículo es de tipo:",self.tipo,", marca:",self.marca,", modelo:",self.modelo)
    
    def avanza(self,velocidad_de_avance):
        velocidad=velocidad_de_avance
        print(f"El Vehículo:",self.tipo,", marca:",self.marca,", modelo:",self.modelo,", se encuentra en movimiento a",velocidad,"Km/h")

automovil= Vehiculos("Terrestre","Ford","Focus")
automovil.caracteristicas()
automovil.avanza(120)
avion= Vehiculos("Aereo","Boeing","747")
avion.caracteristicas()
avion.avanza(850)

# Clase 2---------

class Animales:
    def __init__(self,nombre,tipo,raza,edad):
        tipo_alimentacion=""
        self.nombre=nombre
        self.tipo=tipo
        self.raza=raza
        self.edad=edad

    def caracteristicas(self):
        print(self.nombre,"es un animal de tipo",self.tipo,"es de raza",self.raza,"y tiene",self.edad)
    
    def tipo_alimento(self,alimento):
        
        if alimento == "carne":
            tipo_alimentacion= "carnivoro" 
        elif alimento == "vegetales":
            tipo_alimentacion= "hervivoro"
        elif alimento == "carne y vegetales":
            tipo_alimentacion= "omnivoro"
        else:
            tipo_alimentacion= "desconocida"
        print(f"segun su alimentacion",self.nombre,"es", tipo_alimentacion)
  
        

perro=Animales("Toby","canino","ovejero aleman","10 años")
perro.caracteristicas()
perro.tipo_alimento("carne")
vaca=Animales("Lola","vacuno","Holando Argentino","5 años")
vaca.caracteristicas()
vaca.tipo_alimento("vegetales")

