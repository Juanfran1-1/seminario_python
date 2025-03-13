lista= []
cantidad= int(input("Ingrese cantidad de numeros en la lista: "))
for num in range(cantidad):
    ingresado=int(input("Ingrese numero: "))
    lista += [ingresado]
print(lista)    
listastring=[]
for num in lista:
    if num % 3 != 0:
        listastring+=[str(num)]   
    