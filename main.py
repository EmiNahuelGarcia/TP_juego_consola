import random
import keyboard
from funciones import *
from personajes import *




def elegir_menu():
    '''
    funcion para elegir en el menu
    no toma argumentos
    no retorna nada
    
    '''
    seleccion = ""
    while seleccion != "4":
        print(mostrar_menu())
        seleccion = input("elige una opcion: ")
        match seleccion:

            case "1":
                jugar_juego(heroe)

            case "2":
                print(mostrar_creditos())
            
            case "3":
                print(como_jugar())

            case "4":
                print(salir_juego())
                return
            
            case "5":
                mostrar_puntuacion(historial_puntuacion)

            case _:
                print(f"opcion incorrecta")

def jugar_juego(heroe : dict):
    '''
    funcion para comenzar el juego
    toma un diccionario para nombrar al personaje principal
    retorna el nombre y verifica que el juego se deba ejecutar
    no retorna nada, solo printea
    '''

    heroe['nombre'] = ingresar_nombre(heroe)
    print(f"Bienvenido, {heroe['nombre']}! Prepárate para adentrarte en el laberinto...")
    
    while verificar_vida_boss(enemigos, historial_puntuacion) and verificar_estado_juego(heroe, historial_puntuacion):
        accion = tomar_accion()
        efecto_accion(accion)

        



elegir_menu()


