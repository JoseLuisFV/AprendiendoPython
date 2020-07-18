#Ejercicio Platzi 2
def es_primo(numero):
    contador = 0

    for num in range(1, numero + 1):
        print('numero')
        if numero == 2:
            return True
        if num == 1 or num == numero:
            continue
        if numero % num == 0:
            return False
    return True



def main():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('El Numero es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    main()