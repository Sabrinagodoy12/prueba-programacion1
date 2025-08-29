#Primero validar la igualdad, despues tomar 1 jugador por referencia y ver todas las opciones: jugador1 piedra, el otro tijera, ganó el 1...

print("¡Jugaremos piedra papel o tijera!")
jugador1 = input("Seleccione cuál usará en esta ronda: Piedra  Papel  Tijera ").lower()
jugador2 = input("Seleccione cuál usará en esta ronda:  Piedra  Papel  Tijera pie").lower()

if (jugador1 == "tijera" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "papel") or (jugador1 == "piedra" and jugador2 == "piedra"):
    print("Empate!")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
    print("Gana el jugador 1!")
else : 
    print("Gana el 2")
    
#.strip() para sacar los espacios 
