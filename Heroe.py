import random

from Personaje import Personaje


# La Manera para hacer uso de herencia es escribiendo en parerentesis
# la clase o clases de las que queremos heredar
class Heroe(Personaje):
    # El contructor en pythons se declara con def __init__
    # en donde en parentesis va el self esta palabra reservada
    # para referirse a esta clase, tambien, van los parametros
    # que se nesecitan para poder crear un objeto de esta clase

    def __init__(self, name, job):
        # El constructor sirve para que se haga toodo lo necesario que
        # queramos que se haga ya sea si queremos inicializarle variables
        # o ejecutar funciones

        # De esta manera mandamos hacemos uso del contructor, de la clase que se esta
        # heredando
        super().__init__(name, job)

        # Para declarar variables privadas solo se necesita colocar doble "_"
        self.__atack = 0
        self.__defense = 0
        self.__speed = 0
        self.items = ['Mapa']
        # Tambien se pueden usar metodos que queremos ejecutar al momento de su creacion
        self.__generar_stats()

    # Los metodos tambien tienen su tipo de acceso ya sea publico, protected o privado
    # Ha presentacion de le aplico polimorfismo.
    def presentacion(self):
        print(f'Hola soy {self.name} y estoy en mi aventura como {self.job}'
              '\nAndo en busca de companeros para vencer al mal de este mundo')

    def __generar_stats(self):
        for punto in range(18):
            probabilidad = random.randint(0, 2)
            if probabilidad == 0:
                self.__atack += 1
            elif probabilidad == 1:
                self.__defense += 1
            elif probabilidad == 2:
                self.__speed += 1

    def ver_mis_stats(self):
        print(f'Nombre {self.name} '
              f'\nAtaque: {self.__atack}'
              f'\nDefensa: {self.__defense}'
              f'\nVelocidad: {self.__speed}')

    def recoger_items(self, item):
        if len(self.items) < 20:
            self.items.append(item)
            print(f'Obtuviste {item}')
        else:
            print('Tienes tu bolsa de items llena')

    def ver_mis_items(self):
        for item in self.items:
            print(item)

    def atacar(self):
        return self.__atack + random.randint(0, 3)
