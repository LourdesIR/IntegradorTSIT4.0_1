# importamos la lista para poder realizar el promedio.

# import lista as l                  # Si no se llama "lista modificar nombre"

#-------- Funcion promedio ---------
def fn_promedio(lista):
    suma=0                         # Variable que almacena el valor de la suma.
    for i in lista:              # Bucle para sumar los elementos de la lista.
        suma += i
    resultado=suma/len(lista)    # Variable que hace el promedio de la lista.
    return resultado       # Retorna el valor de resultado - "eliminar print si es necesario".    


