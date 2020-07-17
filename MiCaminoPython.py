# Ejercicio 2 Platzi
def palindromo(palabra):
    #La funcion replace que viene ya definida en python y remplaza
    #los caracteres iguales al primer parametro por caracteres iguales
    #a los del segundo argumento
    palabra = palabra.replace(' ', '')
    #Funcion que pone en minuscula todas las letras
    palabra = palabra.lower()
    #Ingresa lo que hay en la variable palabra pero la ingresara
    #haciendo que la ultima letra de esta variable, sea la primera
    #para la nueva variable
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es Palindromo')

    else:
        print('No Es Palindromo')


if __name__ == '__main__':
    main()