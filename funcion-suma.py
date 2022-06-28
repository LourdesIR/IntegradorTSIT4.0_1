def sumar_lista(lista):
    "Esta función suma todos los elementos de la lista"
    suma = 0 

    for numero in lista:
        suma += numero

    return suma

 
numeros_lista= [58, 27, 248, 77, 12]   
print(sumar_lista(numeros_lista))



