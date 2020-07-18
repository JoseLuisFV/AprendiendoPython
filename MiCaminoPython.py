#Ejercicio Platzi 2
import random
def generated_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)

    print(password)


def main():
    generated_password()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for vector in matrix:
        for num in vector:
            print(num)


if __name__ == '__main__':
    main()