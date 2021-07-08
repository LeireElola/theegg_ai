"""
Lenguaje de programación: Python 3
Tarea 33: Dibujar y programar un combate Pokemon.
Fecha: 07/07/2021
"""
import random
#Inicializamos los variables con sus valores
vidapikachu=int(100)
vidagiglipop=int(100)
ataquepikachu=int(55)
ataquegiglipop=int(45)
ronda=int(1)
#El la función principal, llamaremos a la función combate e indicaremos el ganador del juego
def main():
    #Incializamos los variables como globales para que su valor cambie con las distintas operaciones que se realizan en las funciones.
    global vidapikachu
    global vidagiglipop

    print("Vienvenido al juego de Pikachu, comenzamos con el combate !!")
    #Hata que la vida de algun pockemon sea menor o igual a 0, se disputa el combate
    while vidapikachu>0 and vidagiglipop>0:
        #Llamamos a la función combate
        combate()
    #Quien haya obtenido mayor puntuación, será el ganador del combate
    if (vidapikachu>vidagiglipop):
        print("El ganador es Pikachu con", vidapikachu,"puntos. Zorionak!")
    else:
        print("El ganador es Giglipop con",vidagiglipop,"puntos. Zorionak!")
#En la función combate, calcularemos el turno y realizaremos operaciones hasta que uno de los dos pockemons pierda el juego
def combate ():
    #Inicializamos los valores como globales
    global vidapikachu
    global vidagiglipop
    global ronda
    #Calculamos el turno aleatoriamente
    turno=random.randint(0,1)
    print("comenzamos con la ronda numero:", ronda)
    if turno==1:
        #Si el tunro es 1, el ataque es de Pikachu, por lo que restamos el ataque a la vida de Giglipop
        print("Ataque de Pikachu")
        vidagiglipop=vidagiglipop-ataquepikachu
        print("vida de Pikachu",vidapikachu, " / Vida Giglipop", vidagiglipop)
        ronda=ronda+1
    else:
        #Si el tunro es 0, el ataque es de Giglipop, por lo que restamos el ataque a la vida de Pikachu
        print("Ataque de Giglipop")
        vidapikachu=vidapikachu-ataquegiglipop
        print("vida de Pikachu",vidapikachu, "/ Vida Giglipop", vidagiglipop)
        ronda=ronda+1
while True:
    #llamamos a la función principal
    main()
    if int(input("EXIT [0] / START [1]")):
        #Si el usuario decide continuar, inicializamos los valores
        vidagiglipop=100
        vidapikachu=100
        ronda=1
    else:
        #Si el usuario selecciona salir, termina el juego
        print("Hasta la proxima!")
        break
