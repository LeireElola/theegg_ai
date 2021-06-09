"""
Lenguaje de programación: Python 3
Descripción del programa:
Es un programa que dado un número introducido entre 0,0001 y 0,9999 (no más de 4 cifras decimales),obtiene y muestra la correspondiente fracción irreducible.
"""
#Vemos que la fracción mínima es de 1/10000 y la máxima 9999/10000, por ello tendremos que multiplicar y restar todo con el 10000 (Sólo 4 decimales)
#Declaramos variables globales para que puedan ser utilizados por diferentes funciones.
#Damos valor al denominador. Debido a que vamos a multiplicar por 10000 en el numerador es necesario dividir por el mismo valor si queremos conseguir el resultado intrpducido por el usuario
#el denominador será un constante
zatitzailea=int(10000)
zatikia=int(0)
j=int(0)
#Emepezamos a definir las funciones de nuestro programa
#A la función princiapl le vamos a llamar main, en ella pediremos el valor al usuario y realizaremos las validaciones correspondientes.
def main ():
    print("Introduzca un número entre 0.0001 y 0.9999:")
    #Validamos si el valor introducido por el usuario es un valor float
    try:
        #Si el valor es correcto,damos valor al numerador. multiplicando el valor introducido por el usuario por 10000.De esta manera conseguimos un valor entero
        num=float(input(" "))
        zatikia = int(num*10000)
        j=zatikia
        #Llamamos a la función que reaizará más validaciones sobre el valor introducido por el usuario
        konparaketa(num, zatikia,zatitzailea,j)
    except Exception:
        #Si el valor es erróneo, el sistema le devolverá un mensaje
        print("El valor introducido no es correcto")
#En estea función validamos si el número entra dentro del rango definido y si sólo tiene 4 decimales
def konparaketa (num, zatikia, zatitzailea,j):
    if num<0.0001 or  num>0.9999:
        print("El número introducido no es correcto")
    else:
        if len(str(num)) > 6:
            print("Como máximo se aceptan 4 decimales")
        else :
            #Si todo es correcto, llamamos a la función calculo
            kalkulua (zatikia, zatitzailea, j)
#Esta función se encarga de realizar los cálculos necesarios para conseguir la fracción irreducible
def kalkulua (zatikia, zatitzailea, j):
    #No paramos hasta que el contador sea como mínimo 1, para no deividir con 0 y obetener el menor valor
    while j>0:
        #si el resto de la división entre el numerador y denominador entre j es igual a 0, siginifica que son múltiples por lo que el valor será entero.
        if zatikia%j==0 and zatitzailea%j==0:
            #realizamos las divisiones hasta encontrar el menor valor entero
            zatikia=zatikia/j
            zatitzailea=zatitzailea/j
        #Disminuimos el contador en 1 cada vuelta.
        j=j-1
    #Se imprime la solucón
    print("La fracción irreducible es:", zatikia,"/",zatitzailea)
#Hasta que el usuario no diga lo contrario, ejecutamos el programa
while True:
    #llamamos a la función principal
        main()
        if not int(input("EXIT [0] / START [1]")):
            #Si el usuario selecciona salir, termina el programa
            print("Hasta la próxima!")
            break
