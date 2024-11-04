import random
import keyboard

# Enemigos
enemigos = {
    "Esqueleto": {
        "vida": 35,
        "vida maxima":35,
        "ataque": 10,
        "defensa": 2
        },
    "Goblin": {
        "vida": 30,
        "vida maxima": 30,
        "ataque": 8,
        "defensa": 3
        },
    "Troll": {
        "vida": 55,
        "vida maxima": 55,
        "ataque": 13,
        "defensa": 8
        },
    "Slime": {
        "vida": 15,
        "vida maxima": 15,
        "ataque": 6,
        "defensa": 2
        },
    "Lobo": {
        "vida": 28,
        "vida maxima": 28,
        "ataque": 10,
        "defensa": 2
        },
    "Zombie": {
        "vida": 25,
        "vida maxima": 25,
        "ataque": 8,
        "defensa": 4
        },    
    "Rey Demonio": {  
        'vida': 100,
        'vida maxima': 100,
        'ataque': 10,
        'defensa': 10,
    }
}

# heroe
heroe = {
    "nombre": "",
    "vida": 100,
    "vida maxima": 100,
    "ataque": 13,
    "defensa": 2,
    "inventario": {"pocion": 1},  
    "puntuacion": 0,
    "eventos": 0
}


#objetos
objetos = ["Piedra afiladora", "Mejora de armadura", "Anillo de vida", "pocion", "nada"]
# encuentro random
opciones_encuentro = ["enemigo"] * 2 + ["trampa"] + ["objeto"] * 2

opciones_combate = ["atacar", "tomar pocion", "pedir piedad"]

historial_puntuacion = []


minimo = 0




def mostrar_menu():
    return(f'''
    Laberinto Developers
    1: JUGAR
    2: CREDITOS
    3: COMO JUGAR
    4: SALIR
    5: MOSTRAR PUNTUACION
    ''')
    


def burbuja(historial):
    n = len(historial)
    for i in range(n):
        for j in range(0, n-i-1):
            if historial[j][1] < historial[j+1][1]: 
                
                historial[j], historial[j+1] = historial[j+1], historial[j]   


def mostrar_puntuacion(historial_puntuacion):
    if not historial_puntuacion:
        print(f"Todavia no hay jugadores en el ranking")
    else:
        burbuja(historial_puntuacion)
        for puntuacion in historial_puntuacion:
            print(puntuacion)
    

def elegir_menu():
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

    

def mostrar_creditos():
    
    return f'''
    espero que disfruten este juego, fue hecho con cariño
    desarrolladores del equipo devolopers : 
    Emiliano Garcia
    Daiana Colque
    Valentina Medina
    (derechos reservados)
'''

def como_jugar():
    return f'''
    cada turno elegiras si avanzar o descansar para tomar un objeto
    cada vez que avances tendras la oportunidad de vivir un evento o encontrar un enemigo..
    ganaras puntaje por cada interaccion, mientras mas sobrevivas mejor
    ganas si derrotas al boss final
    '''

def salir_juego():

    print(("Gracias por haber jugado nuestro juego, Presiona una tecla para salir"))
    keyboard.read_event()
    

def reiniciar_heroe(heroe: dict):
    """Reinicia las estadísticas del héroe a sus valores iniciales."""
    heroe['vida'] = 100
    heroe['vida maxima'] = 100
    heroe['ataque'] = 13
    heroe['defensa'] = 2
    heroe['inventario'] = {"pocion": 1}  # Reiniciar el inventario
    heroe['eventos'] = 0  # Reiniciar eventos
    heroe['puntuacion'] = 0  # Reiniciar puntuación
    return heroe

def reiniciar_boss(enemigos: dict):
    enemigos['Rey Demonio']['vida'] = 100
    return enemigos
    

def guardar_puntuacion(historial_puntuacion, heroe):
    historial_puntuacion.append([heroe['nombre'], heroe['puntuacion']])
    return historial_puntuacion

def jugar_juego(heroe:dict):

    heroe['nombre'] = ingresar_nombre(heroe)
    print(f"Bienvenido, {heroe['nombre']}! Prepárate para adentrarte en el laberinto...")
    
    while verificar_vida_boss(enemigos, historial_puntuacion) and verificar_estado_juego(heroe, historial_puntuacion):
        accion = tomar_accion()
        efecto_accion(accion)


def verificar_vida_boss(enemigos: dict, historial_puntuacion):
    if enemigos['Rey Demonio']["vida"] > 0:
        return True   
    else:
        guardar_puntuacion(historial_puntuacion, heroe)
        print("HAS GANADO,VENCISTE AL REY DEMONIO!!!")
        reiniciar_boss(enemigos)
        reiniciar_heroe(heroe)        
        
        return False  

def verificar_estado_juego(heroe:dict, historial_puntuacion)->bool:  
    
    if heroe.get("vida", 0) > 0:
        return True   
    else:
        guardar_puntuacion(historial_puntuacion, heroe)
        print("Has muerto...")
        reiniciar_heroe(heroe)
        reiniciar_boss(enemigos)       
        return False  
    
    
def ingresar_nombre(heroe):
    heroe['nombre'] = input("Introduce el nombre de tu héroe: ")
    while len(heroe['nombre']) <= minimo:
        heroe['nombre'] = input("El nombre del heroe no puede estar vacio: ")
    return heroe['nombre']

def tomar_accion():
    accion = input("¿Que eleccion tomas?: (avanzar / descansar): " ).strip().lower()
    while accion not in ["avanzar", "descansar"]:
        accion = input("Opcion equivocada, decide: (avanzar / descansar)" ).strip().lower()
    return accion

def efecto_accion(accion:str):

    if accion == "avanzar":
        evento = random.choice(opciones_encuentro)
        comenzar_evento(evento, heroe)
        modificar_puntuacion(heroe)


    else:
        tomar_descanso()


def tomar_descanso():
    descansando = True
    while descansando:
        print('''
        1: Tomar pocion
        2: Ver inventario
        3: dejar de descansar
        ''')
        eleccion = input("¿Que haras?: ")
        match eleccion:

            case "1":
                tomar_pocion(heroe)
            case "2":
                ver_inventario(heroe)
            case "3":
                print("Continuas tu viaje")
                descansando = False
                return
            case _:
                print("Opcion erronea")

def tomar_pocion(heroe: dict):

    if heroe['vida'] == heroe['vida maxima']:
        print("Ya tienes la vida al maximo")
        return
    
    elif heroe['inventario']['pocion'] > 0:
        curacion = random.randint(20, 30)
        heroe['vida'] = min(heroe['vida'] + curacion, heroe['vida maxima'])
        heroe['inventario']['pocion'] -= 1
        print(f"Has tomado una pocion. Salud recuperada en {curacion} ahora tienes {heroe['vida']}.")
        return 
    
    else:
        print("No tienes pociones en tu inventario.")       
        return 

def ver_inventario(heroe):

    for pociones, cantidad in heroe['inventario'].items():
        print(f"{pociones}: tienes {cantidad}")

def comenzar_evento(evento, heroe):
    
    if evento == "enemigo":
        enemigo_aleatorio = random.choice(list(enemigos.keys()))
        if enemigo_aleatorio == 'Rey Demonio':          
            print("Te encuentras con el jefe final...")
            if heroe['eventos'] > 10:
                comenzar_combate('Rey Demonio')
            else:
                print("No te sientes listo y escapas...")
                enemigo_aleatorio = random.choice(list(enemigos.keys()))

            
        else:
            print(f"Te encuentras con un {enemigo_aleatorio} salvaje!!!")
            comenzar_combate(enemigo_aleatorio)
            modificar_puntuacion(heroe)
        
    
    elif evento == "trampa":
        daño = random.randint(1, 5)
        heroe['vida'] = max(heroe['vida'] - daño, 0) 
        print(f"Has caído en una trampa y has perdido {daño} de vida. Vida restante: {heroe['vida']}")
        
    else: 
        objeto_aleatorio = random.choice(objetos)
        if objeto_aleatorio == "nada":
            print(f"no encontraste nada..")
        else:
            print(f"Has encontrado un objeto: {objeto_aleatorio} y 10 puntos!!!")
            obtener_objeto(objeto_aleatorio, heroe)
            modificar_puntuacion(heroe)


def comenzar_combate(enemigo):
    
    nombre_monstruo = enemigo
    monstruo = enemigos[enemigo]
    monstruo['vida'] = monstruo['vida maxima']
    
    for estadisticas, valor in monstruo.items():
        print(f"{estadisticas.capitalize()}: {valor}")
    while monstruo['vida'] > 0 and heroe['vida'] > 0:
        accion_combate = elegir_accion_combate()
            
        if accion_combate == "atacar":
            dar_ataque(heroe, nombre_monstruo, monstruo)
            if monstruo['vida'] > 0:
                recibir_ataque(monstruo, nombre_monstruo, heroe)
            else:
                print(f"Enemigo derrotado! ganas 10 puntos")
                
        elif accion_combate == "pedir piedad":
            if pedir_piedad() == False:
                print("Has pedido piedad al enemigo y escapas. El combate termina.")
                break
            else:
                recibir_ataque(monstruo, nombre_monstruo, heroe)

        else:
            tomar_pocion(heroe)

def obtener_objeto(objeto,heroe):

    if objeto == "Piedra afiladora":
        mejorar_ataque(heroe)

    
    elif objeto == "Mejora de armadura":
        mejorar_armadura(heroe)
        
    
    elif objeto == "Anillo de vida":
        mejorar_vida(heroe)
        

    else:
        obtener_pocion(heroe)
        
    
def modificar_puntuacion(heroe):
    heroe['eventos'] += 1
    heroe['puntuacion'] += 10

def elegir_accion_combate():
    accion_combate = input("Elige una acción: (atacar / tomar pocion / pedir piedad): ").strip().lower()
    while accion_combate not in opciones_combate:
        accion_combate = input("Comando equivocado (atacar / tomar pocion / pedir piedad): ").strip().lower()
    return accion_combate

def dar_ataque(heroe, nombre_monstruo, monstruo):
    daño_infligido = max(0, heroe['ataque'] - monstruo['defensa'])
    monstruo['vida'] = max(0, monstruo['vida'] - daño_infligido)  
    print(f"Atacas al {nombre_monstruo} y le infliges {daño_infligido} de daño. Vida restante del enemigo: {monstruo['vida']}.")

def recibir_ataque(enemigo, nombre_monstruo, heroe):
    daño_recibido = max(0, enemigo['ataque'] - heroe['defensa'])
    heroe['vida'] = max(heroe['vida'] - daño_recibido, 0)
    print(f"El {nombre_monstruo} te ataca y te inflige {daño_recibido} de daño. Vida restante: {heroe['vida']}.")

def pedir_piedad():
    piedad = ["no tuvo piedad"] * 2 + ["tuvo piedad"]
    decision_monstruo = random.choice(piedad)
    
    if decision_monstruo == "no tuvo piedad":
        print(f"El monstruo no tuvo piedad")
        return True
    else:    
        return False

def mejorar_ataque(heroe):
    heroe['ataque'] += 2
    print(f"Espada mejorada, tienes {heroe['ataque']} de ataque")

def mejorar_armadura(heroe):
    heroe['defensa'] += 2
    print(f"Armadura mejorada, tienes {heroe['defensa']} de defensa")

def mejorar_vida(heroe):
    heroe['vida'] += 30
    heroe['vida maxima'] += 30       
    print(f"Vida maxima mejorada, tienes {heroe['vida maxima']} de vida maxima y {heroe['vida']} de vida")

def obtener_pocion(heroe):
    heroe['inventario']['pocion'] += 1
    print(f"Pocion agregada al inventario, ahora tienes {heroe['inventario']['pocion']}")



    


    


elegir_menu()


