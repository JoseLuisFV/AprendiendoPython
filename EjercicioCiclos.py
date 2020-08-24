import math

# Ejercicio 1
# Muestra los numeros multiplos de 5 de 0 a 100 utilizando un bucle for
for number in range(0, 101):
    es_multiplo = (number % 5) == 0
    if es_multiplo:
        print(number)

# Ejercicio 2
# Muestra los numeros multiplos de 5 de 0 a 100 utilizando un bucle while
number = 0
while number <= 100:
    es_multiplo = (number % 5) == 0
    if es_multiplo:
        print(number)
    number += 1

# Ejercicio 3
# Muestra los numeros del 320 al 160, contanto de 20 en 20 hacia atras for
for number in range(320, 159, -20):
    print(number)

# Ejercicio 4
# Muestra los numeros del 320 al 160, contanto de 20 en 20 hacia atras while
number = 320
while number >= 160:
    print(number)
    number -= 20

# Ejercicio 5
# Realiza el control de acceso a una caja fuerte. La combinación será un
# número de 4 cifras. El programa nos pedirá la combinación para abrirla. Si no
# acertamos, se nos mostrará el mensaje “Lo siento, esa no es la combinación”
# y si acertamos se nos dirá “La caja fuerte se ha abierto satisfactoriamente”.
# Tendremos cuatro oportunidades para abrir la caja fuerte.
combinacion_de_caja = 1234
intentos = 1
caja_abierta = False
mensaje = 'Lo siento, esa no es la combinacion'
while intentos <= 4:
    combinacion_de_usuario = int(input('Adivina la combiancion: '))
    if combinacion_de_usuario == combinacion_de_caja:
        mensaje = 'La Caja fuerte se ha abierto exitosamente'
        caja_abierta = True
        break
    print(mensaje)
    intentos += 1
if caja_abierta:
    print(mensaje)

# Ejercicio 6
# Muestra la tabla de multiplicar de un número introducido por teclado.
numero_a_multiplicar = int(input('Ingrese el numero que desee multiplicar: '))
for number in range(0, 11):
    print('La multplicacion de ' + str(numero_a_multiplicar) + 'x' + str(number)
          + ' es ' + str(numero_a_multiplicar*number))

# Ejercicio 7
# Realiza un programa que nos diga cuántos dígitos tiene un número introducido
# por teclado.
cifra = input('Escribe una cifra numerica entera: ')
cantidad_de_digitos = 0
for digito in cifra:
    cantidad_de_digitos += 1
print('Tu Numero Tiene ' + str(cantidad_de_digitos))

# Ejercicio 8
# Escribe un programa que calcule la media de un conjunto de números positivos
# introducidos por teclado. A priori, el programa no sabe cuántos números se
# introducirán. El usuario indicará que ha terminado de introducir los datos
# cuando meta un número negativo.
seguir_ciclo = True
suma = 0
divisor = 0
print('Haz iniciado el programa para obtener el promedio de una serie de numeros')
while seguir_ciclo:
    print('Si quieres terminar el ingreso de datos basta con escribir cualquier '
          'numero negativo')
    numero = int(input('Ingresa el numero: '))
    if numero < 0:
        seguir_ciclo = False
    else:
        suma += numero
        divisor += 1
promedio = suma/divisor
print('El promedio fue ' + str(promedio))

# Ejercicip 9
# Escribe un programa que muestre en tres columnas, el cuadrado y el cubo de
# los 5 primeros números enteros a partir de uno que se introduce por teclado.
print('Escribe un numero del cual conoceras el cuadrado y el cubo los 5 siguientes'
      '\nenteros')
number = int(input("Ingresa el numero: "))
tabla = '| numero | cuadradro | cubo |'
for numero_n in range((number + 1), (number + 6)):
    cuadrado = math.pow(numero_n, 2)
    cubo = math.pow(numero_n, 3)
    tabla += "\n|  " + str(numero_n) + '  |' + '  ' + str(cuadrado) + '  ' + '|  ' + str(cubo) + '  |'
print(tabla)
# Ejercicio 10
# Escribe un programa que muestre los n primeros términos de la serie de
# Fibonacci. El primer término de la serie de Fibonacci es 0, el segundo es 1
# y el resto se calcula sumando los dos anteriores, por lo que tendríamos que
# los términos son 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144… El número n se
# debe introducir por teclado
numero_para_fibonacci = int(input('Ingresa los n numeros que quieras de una serie'
                                  'de finabocci: '))
numero_anterior = 0
numero_anterior_anterior = 0
for number in range(0, numero_para_fibonacci):
    if numero_anterior != 0:
        numero_para_fibonacci = numero_anterior + numero_anterior_anterior
    else:
        numero_para_fibonacci = number
    numero_anterior_anterior = numero_anterior
    numero_anterior = numero_para_fibonacci
    print(str(numero_para_fibonacci))
