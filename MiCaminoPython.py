# Este programa abarca listas
# forma de declarar listas
videogames_characters = ["Mario", "Sonic", "Master Chief", "Marcus Fenix",
                         "Cratos", "Cayde-6", "San-14", "Joker Persona 5"]
#Con la funcion len obtenemos la cantidad de personajes que tiene la lista
print(len(videogames_characters))
#Se Elige el primer personaje de la lista

character = videogames_characters[0]
print(character)

#Se Elige el ultimo personaje de la lista
character = videogames_characters[-1]
print(character)
#Se Elige el ultimo personaje de la lista
character = videogames_characters[-2]
print(character)
#En python tenemos una manera interesante de obtener un conjunto de variables
#existentes en la lista y eso es utilizando limites de donde las queremos agarrar
#pero el simbolo que nos ayuda a esto es el ":", el cual del lado izquierdo
#el limite inferior a la izquierda y el limite superior a la derecha

#el siguiente codigo imprimer el conjuntos de variables que se encuentran a partir
# de lo posicion 3, eso incluye lo que hay en esta misma posicion
print(videogames_characters[4:])
#el siguiente es parecido perso toma las que se encuentran abajo de esta posicion
# pero en este caso no se incluye la que se encuentra en esata misma
print(videogames_characters[:4])
#Por ultimo le podemos dar ambos limites
print(videogames_characters[2:6])

#podemos modificar una de las variables por otra
videogames_characters[6] = "Link"
print(videogames_characters)
