Laberinto Developers
¡Bienvenido a Laberinto Developers!
Un juego de aventuras en el que encarnas a un héroe en un misterioso laberinto lleno de peligros, tesoros y el gran desafío de derrotar al Rey Demonio. ¿Tienes lo que se necesita para sobrevivir y convertirte en el campeón del laberinto?

📖 Historia del Juego
Te despiertas en un oscuro laberinto sin memoria de cómo llegaste allí. Para salir, deberás enfrentarte a enemigos, evitar trampas y mejorar tus habilidades recogiendo objetos. Tu destino final: el Rey Demonio, el jefe final que pondrá a prueba tu valentía y fuerza.

🎮 Cómo Jugar
Inicio del juego:
Al iniciar el juego, se te presentará un menú principal con las siguientes opciones:

1: JUGAR: Comienza tu aventura.
2: CREDITOS: Ve los créditos del equipo desarrollador.
3: COMO JUGAR: Aprende las reglas y mecánicas del juego.
4: SALIR: Sal del juego.
5: MOSTRAR PUNTUACIÓN: Visualiza el ranking de puntuaciones.
Durante el juego:

Cada turno podrás avanzar o descansar:
Avanzar: Puede resultar en un encuentro con un enemigo, una trampa o un objeto. Cada interacción te otorga puntos.
Descansar: Puedes tomar pociones, ver tu inventario o prepararte antes de continuar.
Los enemigos serán aleatorios, incluido el temido Rey Demonio. ¡Prepárate para luchar o pedir piedad!
Recoge objetos para mejorar tus estadísticas (ataque, defensa, vida) y obtén pociones para curarte.
Objetivo del juego:

Derrota al Rey Demonio para ganar.
Cuanto más sobrevivas y mejores sean tus decisiones, mayor será tu puntuación.
🛠️ Características del Código
Programación Modular:
El juego está dividido en funciones para mantenerlo organizado y legible.

Sistemas Integrados:

Combate: Mecánica de ataques entre el héroe y los enemigos con posibilidad de pedir piedad.
Gestión de Inventario: Los objetos recogidos mejoran tus estadísticas o aumentan tus recursos.
Eventos Aleatorios: Cada avance puede ser un encuentro peligroso o beneficioso.
Puntuación y Ranking: Guarda las puntuaciones de los jugadores en un historial.
Mecánicas Aleatorias:
Las decisiones de los enemigos y los efectos de objetos, trampas o curaciones son aleatorios, haciendo cada partida única.

💾 Estructura del Código
El juego incluye las siguientes funciones principales:

Menú del juego:

mostrar_menu(): Muestra las opciones iniciales.
salir_juego(): Permite salir del juego.
Gestión del héroe y enemigos:

reiniciar_heroe(): Resetea las estadísticas del héroe.
reiniciar_boss(): Resetea las estadísticas del jefe final.
Eventos y mecánicas:

tomar_accion(): Decide si avanzar o descansar.
efecto_accion(): Procesa los efectos de avanzar o descansar.
comenzar_evento(): Determina si encuentras un enemigo, trampa u objeto.
Combate:

comenzar_combate(): Inicia un combate contra un enemigo.
dar_ataque() y recibir_ataque(): Determinan el daño en cada turno.
Objetos y mejoras:

obtener_objeto(): Maneja los objetos encontrados.
mejorar_ataque(), mejorar_armadura(), mejorar_vida(), obtener_pocion(): Mejoran las estadísticas o recursos del héroe.
Puntuación:

guardar_puntuacion(): Guarda la puntuación del héroe.
mostrar_puntuacion(): Muestra el ranking de puntuaciones.
📋 Requisitos del Sistema
Python 3.x
Módulo random (nativo de Python)
Teclado funcional para interacciones en el juego (utilizando keyboard si se amplía).
🧑‍💻 Créditos
Este juego fue desarrollado con esfuerzo y dedicación por el equipo Developers InCompany:

Emiliano García
Daiana Colque
¡Buena suerte en tu aventura! 🎲
Espero que disfrutes jugando y desafiando tus habilidades en Laberinto Developers. Si tienes sugerencias o mejoras, ¡no dudes en compartirlas! 🎮✨
