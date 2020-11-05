# Los archivos o files en python se manejan de manera muy 
# sencilla para ello existen dos elemento  que no tenemos que crear 
# de cero el primero es crear un objeto de open()
#
# Donde solo se necesitan minimo 2 argumentos el primero de ellos
# es la ruta junto con el nombre obviamente, y el otro argumento
# es el modo de operacion
#
#  ejemplo
#  mi_archivo = open('C:/miruta/miarchivo.txt', 'mododeoperacion')
# 
# A continuacion lo modos de operacion
# r = Es el modo predeterminado. Abre el archivo para su lectura
# w = Este abre el archivo para escribir, si no existe lo crea
#     si existe trunca el archivo
# a = abre el archivo en modo de anexar, si el archivo 
#     no existe lo creara
# + = Abrira el archivo para leer y escribir(Actualizar)
#
# una vez creado nuestro objeto de tipo Open el podemos utilizar sus funciones
# el segundo elemento importante es su funcion close() el cual se utiliza
# cada vez que hemos terminado de manipular el archivo, por lo tanto ya no 
# necesitaremos y close() se necesita para dejar de usarlo de manera segura
# 
# Ejemplo
# mi_archivo.close()


def add_to_list():
    # existe una manera de acortar el numero de lineas de codigo y es que
    # si escribimos with open('ruta/example/txt', 'operacion') as f:
    # lo que estariamos haciendo es iniciar un bloque de codigo limitado 
    # por identacion y no ocuparemos escribir close
    with open('C:/Users/lui_z/Desktop/food-list.txt', 'a+') as f:
        new_food = input("Write what you want to add: ")
        # con la funcion write es con la que realmente va a escribir, y el 
        # argumento que nosotros pasamos sera lo que se escribira el archivo
        f.write(f'{new_food} \n')


def read_list():
    try:
        with open('C:/Users/lui_z/Desktop/food-list.txt', 'r') as f:
            # utilizamos un for para recorrer todas las lineas del archivo
            # y el print para verlo en consola
            for line in f:
                print(line)
    except FileNotFoundError:
        print(f"Sorry, your file already does not exist, but it will be create right now."
              "\nFor Obviusly reasons it is empty, but now you can fill it and read anytime you want")
        with open('C:/Users/lui_z/Desktop/food-list.txt', 'w+'):
            pass


def my_food_list():
    option = 1
    try:
        option = int(input("1. Read My Food list\n2. Add Food To My List:\n"))
    except ValueError:
        option = 1
        print("You had select a inexist option, then for default we select the read option")
    finally:
        if option == 1:
            read_list()
        elif option == 2:
            add_to_list()


def main():
    main_option = 0
    run = True
    while run:
        my_food_list()
        try:
            main_option = int(input('IF YOUY WANT TO CLOSE THIS PROGRAM WRITE "1": '))
        except ValueError:
            main_option = 0
            print('you did not select the exit option, the program keep running\n')
        finally:
            if main_option == 1:
                run = False


if __name__ == '__main__':
    main()
