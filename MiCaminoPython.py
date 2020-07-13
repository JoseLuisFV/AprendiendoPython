# Utilizamos el bucle for que solo itera las mismas veces
# que la cantidad de palabras que hay en la lista
for char in ["Yo", "Amo", "La", "Robotica"]:
      print(char)
print("")
# aqui vemos un for que  imprime la caneda letra por letra
# y declaramos el una variable para almacenar la letra
# momentanea
for char in "loops":
      print(char)
print("")
# En este ciclo for lo que hacemos es imprimir los numeros del 0 a 19
# para eso almacenamos de manera momentanea los numeros en la variable
# number
for number in range(20):
      print(number)
print("")
# Si se quiere que se impriman numeros de 1 a 20 se le da un inicio y
# final a la funcion range
for number in range(1, 21):
      print(number)
print("")
# esta funcion tiene algo mas intereante y es que se puede indicar el
# incremento que tendra el conjunto de numeros, por ejemplo de a 2
for number in range(10, 21, 2):
      print(number)
