#test_Examen_15_12_jaime_benitez_acien



from Examen_15_12_jaime_benitez_acien import filtra_ejercicios, duracion_ejercicios

import pytest

@pytest.mark.parametrize(
    "lista, minutos, resultado", [([{"denominacion": "No hay respiro",
    "descripcion": "Buscamos llegar a tres pases en el equipo para devolver el balón al sacador de banda = 2 ptos.\nEste devolverá el balón al equipo pasador = 1 pto.\n(2x2, 3x3, 4x4...+1)\nVariante: logrados 3 pases en el equipo al pasar al sacador intercambio de funciones.",
    "estrategia": ["Siempre en movimiento.", "Acción para el otro.",
    "Dos actitudes en defensa a descubrir ante diversas valoraciones en el jugar.", "Enriquecer con cortes y su defensa. Chocar los cortes."],
    "duracion": 20}, {"denominacion": "Mensaje",
    "descripcion": "Intentamos pasar el balón a un jugador defendido dentro del círculo.\nSuperioridad atacante.", 
    "estrategia": ["Desmarcarse y buscar línea de pase.", "Sellar el apoyo fuerte del defensor.", 
    "Fijar al defensor y dar referencia."], "duracion": 20},{"denominacion": "Sin parar",
    "descripcion": "4x4, 5x5\nPase al jugador interior e intercambio de posiciones.", 
    "estrategia": ["Interior / Exterior.", "Reemplazar.", "Ganar la entrada del balón en el juego interior.", "Pasar y seguir."],
    "duracion": 10}, {"denominacion": "Las alianzas", 
    "descripcion": "4 x 2 + 2.\n4 atacantes intentan tocar con el balón adaptado a 2.\nDos defensores se lo impiden.", 
    "estrategia": ["Intercepciones de pases.", "Buscarse apoyos"], "duracion": 10}],10,
    [{"denominacion": "Sin parar",
    "descripcion": "4x4, 5x5\nPase al jugador interior e intercambio de posiciones.", 
    "estrategia": ["Interior / Exterior.", "Reemplazar.", "Ganar la entrada del balón en el juego interior.", "Pasar y seguir."],
    "duracion": 10}, {"denominacion": "Las alianzas", 
    "descripcion": "4 x 2 + 2.\n4 atacantes intentan tocar con el balón adaptado a 2.\nDos defensores se lo impiden.",
    "estrategia": ["Intercepciones de pases.", "Buscarse apoyos"], 
    "duracion": 10}])]
)

def test_filtra_ejercicios(lista,minutos,resultado):
    assert filtra_ejercicios(lista,minutos) == resultado , "Filtra correctamente"



@pytest.mark.parametrize(
    "lista, resultado", [([{"denominacion": "No hay respiro",
    "descripcion": "Buscamos llegar a tres pases en el equipo para devolver el balón al sacador de banda = 2 ptos.\nEste devolverá el balón al equipo pasador = 1 pto.\n(2x2, 3x3, 4x4...+1)\nVariante: logrados 3 pases en el equipo al pasar al sacador intercambio de funciones.",
    "estrategia": ["Siempre en movimiento.", "Acción para el otro.",
    "Dos actitudes en defensa a descubrir ante diversas valoraciones en el jugar.", "Enriquecer con cortes y su defensa. Chocar los cortes."],
    "duracion": 20}, {"denominacion": "Mensaje",
    "descripcion": "Intentamos pasar el balón a un jugador defendido dentro del círculo.\nSuperioridad atacante.", 
    "estrategia": ["Desmarcarse y buscar línea de pase.", "Sellar el apoyo fuerte del defensor.", 
    "Fijar al defensor y dar referencia."], "duracion": 20},{"denominacion": "Sin parar",
    "descripcion": "4x4, 5x5\nPase al jugador interior e intercambio de posiciones.", 
    "estrategia": ["Interior / Exterior.", "Reemplazar.", "Ganar la entrada del balón en el juego interior.", "Pasar y seguir."],
    "duracion": 10}, {"denominacion": "Las alianzas", 
    "descripcion": "4 x 2 + 2.\n4 atacantes intentan tocar con el balón adaptado a 2.\nDos defensores se lo impiden.", 
    "estrategia": ["Intercepciones de pases.", "Buscarse apoyos"], "duracion": 10}],60)]
    )

def test_duracion_ejercicios(lista,resultado):
    assert duracion_ejercicios(lista) == resultado , "Funciona correctamente"