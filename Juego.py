#PIEDRA, PAPEL O TIJERAS

nombre_1 = input("Nombre del jugador 1: ")
nombre_2 = input("Nombre del jugador 2: ")
jugador_1 = input(nombre_1 + " " + "Elige una opcion: 1-piedra, 2-papel o 3-tijeras: ")
jugador_2 = input (nombre_2 + " " + "Elige una opcion: 1-piedra, 2-papel o 3-tijeras: ")

if jugador_1 == jugador_2:
  print("¡EMPATE!")
elif (jugador_1 == 3 and jugador_2 == 2) or (jugador_1 == 1 and jugador_2 == 3):
  print("¡Gano el jugador" + " " + nombre_1)
else:
  print("¡Gano el jugador" + " " + nombre_2)




