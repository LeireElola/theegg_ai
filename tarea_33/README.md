Para poder ejecutar el código, es necesario tener descargado Python 3. Lo podrás descargar desde el siguiente link: 
https://www.python.org/downloads/

Una vez tengas python 3, podrás ejecutar el código en cmd (py nombrefichero.py) o en cualquier editor de código.

Tal y como se puede ver en el digarama de flujo, se trata de un juego Pockemon donde solamente 2 jugadores podrán combatir.

 1. Valores inicio:
	Vida Pikachu=100
	Vida Giglipop=100
	Ataque Pkachu=55
	Ataque Giglipop=45
	Ronda=1 (Esta variable la utilizaremos para saber en que ronda estamos)

2.Calculamos el turno en modo aleatorio.
	Si Turno=1 -> Ataca Pikachu
	Si Turno=0 -> Ataca Giglipop

3. Al atacar se reducirá la vida del otro pokemon, por el importe del ataque correspondiente.

4. Esto se repite hasta que uno de los dos pokemons se quede si vida. 

5.Gana el Pokemon con más puntos.