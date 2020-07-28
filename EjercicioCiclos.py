#Ejercicio 1
#Muestra los numeros multiplos de 5 de 0 a 100 utilizando un bucle for
for number in range(0, 101):
    es_multiplo = (number%5) == 0
    if es_multiplo:
        print(number)

#Ejercicio 2
#Muestra los numeros multiplos de 5 de 0 a 100 utilizando un bucle while
number = 0
while number <= 100:
    es_multiplo = (number % 5) == 0
    if es_multiplo:
        print(number)
    number += 1

#Ejercicio 3
#Muestra los numeros del 320 al 160, contanto de 20 en 20 hacia atras for
for number in range(320, 159, -20):
    print(number)

number = 320
while number >= 160:
    print(number)
    number -= 20