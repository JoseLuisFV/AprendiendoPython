# ejercicio while donde el usuario debe adivinar un numero y tiene
# 3 intentos donde si no adivina obtiene un mensaje de que fallo
# todas sus oportunidades, la siguiente opcion es que si gana al
# final le enviemos un mensaje de fuertudo y si gana antes de eso
# solo recibe felicitaciones
numero_a_adivinar = 19
intento = 1
print("Bienvenido a tu muerte, pero si adivinas se te da otra vida")
while intento <= 3:
      numero_adivinado = int(input("Elige cualquier numero y prueba "
                                    "tu suerte: "))
      intento += 1
      if numero_a_adivinar == numero_adivinado:
            print("Wow!, Mirate, Genio!")
            break
      else:
            print("No!, Ni en un millon de años!, intetalo de nuevo")
else:
      print("Se te acabaron las oportunidades")


