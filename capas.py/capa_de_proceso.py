import capa_de_proceso
print("jugador1 - por favor elige: piedra,papel o tijera.")
jugador1=input().lower()
print("jugador2 - por favor elige: piedra,papel o tijera.")
jugador2=input().lower()
if jugador1 not in ("piedra","papel","tijera"):
    print("jugador1- por favor elige piedra,papel o tijera.")
elif jugador2 not in ("piedra","papel","tijera"):
    print("jugador2- por favor elige piedra,papel o tijera.")
else:
 if jugador1==jugador2:
    print("empate.")
 elif (jugador1=='piedra'and jugador2=='tijera') or (jugador1=='papel' and jugador2=='piedra') or (jugador1=='tijera'and jugador2=='papel'):
    print("jugador1 ganó!")
 else:
    print("jugador2 ganó!")
