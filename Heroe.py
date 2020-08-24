import random


class Heroe:

    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.atack = 0
        self.defense = 0
        self.speed = 0
        self.items = ['Mapa']
        self.generar_stats()

    def presentacion(self):
        print(f'Hola soy {self.name} y estoy en mi aventura como {self.job}'
              '\nAndo en busca de companeros para vencer al mal de este mundo')

    def generar_stats(self):
        for punto in range(18):
            probabilidad = random.randint(0, 2)
            if probabilidad == 0:
                self.atack += 1
            elif probabilidad == 1:
                self.defense += 1
            elif probabilidad == 2:
                self.speed += 1

    def ver_mis_stats(self):
        print(f'Nombre {self.name} '
              f'\nAtaque: {self.atack}'
              f'\nDefensa: {self.defense}'
              f'\nVelocidad: {self.speed}')

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
        return self.atack + random.randint(0, 3)
