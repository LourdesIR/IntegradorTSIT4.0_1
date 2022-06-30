# Código integral del proyecto
import lista as l
import funcion_suma as s
import fn_promedio as p
import maximo as ma 
import minimo as mi 

print("____ Bienvenid@ al TP integrador de python básico ____") 
list = l.lista()
print("Su lista es:", list) 
print(f"La suma de sus valores es: {s.sumar_lista(list)},")
print(f"el promedio: {p.fn_promedio(list)}")
print(f"su mínimo y máximo respectivamente son: {mi.minimo(list)} y {ma.maximo(list)}")
print("_______________________________________________________") 