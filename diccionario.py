#crear diccionario
midiccionario={"nombre":"Byron", "apellido":"Sosa", "sexo":"masculino"}
print(midiccionario)
#añadir valores
midiccionario["pais"]="Costa Rica"
print(midiccionario)

#eliminar valores
del midiccionario["apellido"]
print(midiccionario)

#obtener claves
print(midiccionario.keys())

#obtener valores
print(midiccionario.values())

#saber longitud del diccionario
print(len(midiccionario))



