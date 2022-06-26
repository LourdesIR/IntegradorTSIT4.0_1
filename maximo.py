#Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de
#todos los elementos que contiene.

def maximo(lista):
     max=0
     for x in lista:
             if x>max : max=x
                                    
     return max
 
#>>> lista=[1,2,3,4,5,6]
#>>> a=maximo(lista)
#>>> print(a)
#6
#>>> 

#### otra forma ####
def Maximo(lista):
     max=0
     for i in range(len(lista)):
            if lista[i]>max: max=lista[i]
     return max
 
#>>> lista=[9,4,5,7,9,2]
#>>> print(Maximo(lista))
#9
#>>> 


