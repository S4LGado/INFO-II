"""
Desarrolle un ciclo while infinito
"""
# condicion = True
# 
# while condicion:
#     print("ciclo ejecutado")

"""Cómo protegernos de un ciclo infinito"""

condicion = True
contador = 0
while condicion:
     print("ciclo ejecutado {}".format(contador))
     contador = contador + 1
     if contador == 100: 
        break

"""
Realice un ciclo while con un numero secreto. Cada vez que se ejecuta
un ciclo, el programa pide adivinar el numero, en caso de no ser acertado
se debe mostrar un mensaje diciendo: "Estás atrapado". Y en caso contrario
terminar el ciclo y avisar que el numero es correcto.
"""
#numero_secreto = 999
#numero_usuario = int(input("Ingrese el número secreto: "))
#condicion = (numero_secreto != numero_usuario)
#
#while condicion:
#    print("No es el número correcto")

"""
Realice un ciclo while que imprima los números del 10 al 100, separados por guion(-)
sin salto de linea
10 - 11 - 12 - 13 - ... 100
"""
