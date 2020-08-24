import random

def generate_lineal_function(range_min_x, range_max_x, range_min_y, range_max_y, label_x, label_y):
    m = (range_max_y - range_min_y) / (range_max_x - range_min_x)
    # y = xm + b
    b = range_min_y - (range_min_x * m)
    print("Tu ecuacion lineal es: ")
    print(f"{label_y} = ({label_x})*({m}){label_y}/{label_x} + {b}{label_y}")
    m_and_b = (m, b)
    return m_and_b


def use_lineal_function(m_and_b, label_y, label_x):
    exit = 1
    print("Estas usando tu funcion que generaste")
    while exit != 0:
        print(f"{label_y} = ({label_x})*({str(m_and_b[0])}){label_y}/{label_x} + {str(m_and_b[1])}{label_y}")
        x = float(input(f"Ingresa los {label_x} que quieres convertir a {label_y}"))
        result = x*m_and_b[0] + m_and_b[1]
        print(f"Tu resultado fue {result} {label_y}")
        exit = int(input("SI quieres salir del programa escribe 0"))


def di_hola(name):
    print(f"Hola! {name}")
    print("Bienvenido a mi live en youtube")


def calculate_cube(number):
    return number * number * number


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
    for c in iter({'a': 1, 'b': 2,'c': 3}):
        print(c)

    frutas = ['manzana', 'pera', 'mango']
    iterator = iter(frutas)
    next(iterator)
    next(iterator)
    print(next(iterator))


    estudiantes = {
        'mexico': 10,
        'colombia': 15,
        'puerto_rico': 4
    }
    for pais in estudiantes:
        print(pais)
    for pais in estudiantes.keys():
        print(pais)
    for numero_de_estudiantes in estudiantes.values():
        print(numero_de_estudiantes)
    for pais, numero_de_estudiantes in estudiantes.items():
        print(pais)
        print(numero_de_estudiantes)
    # generated_password()
    # di_hola("Jose Luis")
    # name_label_y = input("Escribe el nombre que correspondera al eje de las y: ")
    # name_label_x = input("Escribe el nombre que correspondera al eje de las x: ")
    # range_max_y = float(input(f"Cual es el rango maximo en {name_label_y}: "))
    # range_min_y = float(input(f"Cual es el rango minimo en {name_label_y}: "))
    # range_max_x = float(input(f"Cual es el rango maximo en {name_label_x}: "))
    # range_min_x = float(input(f"Cual es el rango minimo en {name_label_x}: "))
    # m_and_b = generate_lineal_function(range_min_x, range_max_x, range_min_y, range_max_y, name_label_x, name_label_y)
    # use_lineal_function(m_and_b, name_label_y, name_label_x)

if __name__ == '__main__':
    main()