Para poder ejecutar el código, es necesario tener descargado Python 3. Lo podrás descargar desde el siguiente link: 
https://www.python.org/downloads/

Una vez tengas python 3, podrás ejecutar el código en cmd (py nombrefichero.py) o en cualquier editor de código.

Para poder realizar este código, es importante entender que la operación matemática a utilizar es el máximo comun divisor.

El máximo comun divisor de dos o más números es el número más grande por el que se pueden dividir los dos números.

Para poder conseguirlo estos son los pasos que he seguido:

	1. Pedimos un valor al usuario
	2. Verificamos si cumple las condiciones
		2.1. Ser un float
		2.2. Estar entre 0.0001 y 0.9999
		2.3. Tener como máximo 4 decimales
	3. Si cumple las condiciones, calculamos el máximo comun divisor. 
	  Para ello, vemos que con 4 decimales la fracción mínima es de 1/10000 y la máxima 9999/10000, por ello tendremos que multiplicar y restar todo con el 10000.
	  Seguimos dividiendo los números siempre que el resto de la división sea 0, hasta obtener la fraccion irreducible.



