## Con el input se le puede ingrese
nombre = input("Cual es tu nombre? ")
## la funcion int convierte la cadena en un entero
edad = int(input("Cual es tu edad? "))
ciudad = input("Donde vives? ")
email = input("Ingrese un correo electronico que use")

# Existe una manera convertir todoen cadena y es con f
# al inicicio seguido de ""
print(f"Hola {nombre} un gusto conocerte sabias que tu {edad}"
      f" Si le sumas 1 siempre cambia al tipo que es? ")
