import random


class Villano:

    def __init__(self, name, job, tipo):
        self.name = name
        self.job = job
        self.tipo = tipo
        self.atack = 0
        self.defense = 0
        self.speed = 0
        self.generar_stats()

    def presentacion(self):
        print(f'Al parecer tu aventura acaba aqui!!, yo el gran {self.name}'
              f'\nSoy el {self.job} que no podras vencer, y al fin no abra quien'
              f'detenga nuestro reino del mal')

    def generar_stats(self):
        for punto in range(28):
            probabilidad = random.randint(0, 2)
            if probabilidad == 0:
                if self.tipo == 'agresivo':
                    self.atack += 2
                else:
                    self.atack += 1
            elif probabilidad == 1:
                if self.tipo == 'defensivo':
                    self.atack += 2
                else:
                    self.atack += 1
            elif probabilidad == 2:
                if self.tipo == 'veloz':
                    self.atack += 2
                else:
                    self.atack += 1

    def ver_informacion(self):
        print(f'Nombre : {self.name}'
              f'\nTipo: {self.tipo}'
              f'\nAtaque: {self.atack}'
              f'\nDefensa: {self.defense}'
              f'\nVelocidad: {self.speed}')

    def function_void(self):
        pass
