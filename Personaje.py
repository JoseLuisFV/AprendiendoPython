class Personaje:

    def __init__(self, name, job):
        self._name = name
        self._job = job

    def presentacion(self):
        print(f'Hola me llamo {self._name} y soy{self._job}')

    # La encapsulacion se hace con el decorador property
    # la cual nos ayuda a utilizarla como getter, ya que retorna
    # la variables que tengan restricciones de accseso
    @property
    def name(self):
        return self._name

    @property
    def job(self):
        return self._job

    # Gracias a que antes se hizo una funcion con el decorador property
    # ahora podemos crear uno con el setter, este decorador se compone, con
    # el nombre de la funcion que le hayamos agregador el decorador property
    # y depues le escribimos ".setter" y el setter nos ayuda a dar cierta restricciones
    # en este caso estamos restringiendo a que "job" sea de tipo "str".
    @job.setter
    def job(self, job):
        if isinstance(job, str):
            self._job = job
        else:
            print("Something went wrong, job should be str type")
