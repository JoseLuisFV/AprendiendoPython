
password = input("Write your new password: ")
print("welcome again on OnFireNews")
password_auth = input("Write your password: ")
# Manera en como se declara la declaracion "if"
if password == password_auth:
      print("Congrats you are learning")
else:
      print("error password didnt match")

number = int(input("Choose a number between 1 to 3: "))

# Declaracion de un if con mas de dos posibilidades
if number == 1:
      print("No hubo suerte ")
elif number == 2:
      print("ganaste")
      other_number = int(input("Pero antes dinos que otro numero hubieras "
                           "escrio: "))
      if other_number == 1:
            print("Excelente ahora si ganaste")
      elif other_number == 3:
            print("Mala eleccion se te dara un cuarto del premio")
      else:
            print("Estaba hablando de las otras dos opciones baboso")
elif number == 3:
      print("No Pienses muy Grande")
else:
      print("You dont know read or what")