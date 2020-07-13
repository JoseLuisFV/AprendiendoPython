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
      if numero_a_adivinar == numero_adivinado:
            if intento < 3:
                  print("Felicidades Ganaste, al parecer tienes talento")
                  intento = 3
            else:
                  print("Eres un ***dito suertudo, Ganaste "
                        "en ultimo intento")
      else:
            if intento < 3:
                  print("Mala suerte intentalo de nuevo")
            else:
                  print("Se te acabaron las oportunidades, no hay vuelta "
                        "atras a tu destino")
      intento += 1


