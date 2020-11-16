midiccionario={}
contador=int(input("Cuantos datos desea añadir: "))
inicial=0

while inicial < contador:
    clave=input("digite el identificador: ")
    valor=input("digite l que desea guardar: ")
    midiccionario[clave]=valor
    inicial+=1

print(midiccionario)