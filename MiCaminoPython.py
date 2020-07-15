# Los diccionarios son como tal cual un conjunto de variables que como
# objetivo deben de tener una relacion entre si, los diccionarios tienen
# dentro de ellos varaibles que se componen con par de datos, uno que es
# como un tipo identificador y el otro sera el valor de interes que queremos
# guardar
user = {
    "nombre": "James",
    "edad": 30,
    "Correo electronico": "james@domain.com",
    "Coche": "Tesla T1"
}

# Se accede a este valor escribiendo el valor que lo identifica, pero de la
# siguiente forma, solo que arrojara un error muy horrible si tal identificador
# no existe
print(user["Correo electronico"])

# Con el metodo get evitamos este error horrible
print(user.get("nombre"))

# Les podemos dar un nuevo par de valores a diccionario si es
print(user.get("dob","1,1,1900"))

# Los diccionarios pueden ser modificables como las listas
for value in user:
    if value == "nombre":
        user[value] = input("Escribe tu nuevo Nombre: ")
    elif value == "edad":
        user[value] = int(input("Escribe tu Nueva edad: "))
    elif value == "Correo electronico":
        variable_temporal = input("Escribe tu nuevo correo: ")
        user[value] = variable_temporal
    elif value == "Coche":
        variable_temporal = input("Escribe el coche que tienes ahora: ")
        user[value] = variable_temporal
    else:
        print("No se encontro nada")

print(user)