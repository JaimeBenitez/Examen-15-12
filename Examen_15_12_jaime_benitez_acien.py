#Examen 15_12 parte 1


import random

def filtra_ejercicios(lista,minutos):
    """
    Recibe: lista = lista de diccionarios  minutos = int
    devuelve: lista 
    Descripción: Función que recibe la lista de diccionarios y un valor de minutos y devuelve todas las entradas de esa lista cuyo 
    valor de la clave "duración" es igual o menor que el parametro "minutos"
    """
    lista_filtrada=[]

    for i in lista:
        if i["duracion"] <= minutos:
            lista_filtrada.append(i)
    return lista_filtrada


def duracion_ejercicios(lista):  
    """
    Recibe: lista = lista de diccionarios
    Devuelve: Int
    Descripción: Función que recibe una lista de diccionarios y realiza la suma de todos los valores de la clave "duración"
    """

    suma_total= sum(i["duracion"] for i in lista)

    return suma_total 


def entrenamiento(lista,minutos):
    """
    Recibe: lista = lista de diccionarios minutos = int
    Devuelve: lista
    Descripción: Función que recibe una lista de diccionarios y un parametro de minutos 
    """

    lista_entrenamiento=[]

    while duracion_ejercicios(lista_entrenamiento) < minutos:
        duracion_restante= minutos - duracion_ejercicios(lista_entrenamiento)
        lista_entrenamiento.append(random.choice(filtra_ejercicios(lista,duracion_restante)))
        
    return lista_entrenamiento    


















