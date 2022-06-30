def lista():
    lista=[]
    i=0
    while i<5:
        num= int(input("ingrese un numero:"))
        lista.append(num)
        i+=1
    return lista   
    
print("su lista es:", lista) 