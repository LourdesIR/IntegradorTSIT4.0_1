#Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de
#todos los elementos que contiene.

def minimo(lista):
     min=lista[0];  
     for i in range(len(lista)):
             if lista[i]<min: min=lista[i]
     return min

#>>> lista=[9,4,5,7,9,2]
#>>> print(minimo(lista))
#2
#>>> lista=[9,4,5,7,9,12]
#>>> 
#>>> print(minimo(lista))
#4
#>>> 

