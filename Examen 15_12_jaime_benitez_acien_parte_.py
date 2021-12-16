#Examen 15_12_jaime_benitez_acien_parte_2

from ejercicios import ejercicios
from Examen_15_12_jaime_benitez_acien import filtra_ejercicios,duracion_ejercicios,entrenamiento
#import json

def nuevo_ejercicio(lista_diccionario:list):
    """
    Recibe: Lista diccionarios
    Devuelve: Nueva entrada
    Descripción: Función que recibe una lista de diccionarios y pide inputs de cada clave para un nuevo diccionario. 
    Finalmente lo añade a la lista y devuelve el nuevo diccionario ya hecho
    """

    denominacion = input("Introduce el nombre del ejercicio: ")
    descripcion = input("Explicanos el ejercicio: ")
    estrategias=[]
    mostrar_input = True
    while mostrar_input:
        estrategia_individual = input("Estrategias a usar en el ejercicio, introduce fin para continuar: ")
        estrategias.append(estrategia_individual)
        if estrategia_individual == "fin":
            mostrar_input = False
        
    duracion = int(input("Introduce duración en min del ejercicio: "))
    ejercicio_nuevo = {"denominacion": denominacion, "descripcion":descripcion, "estrategia": estrategias, "duracion": duracion}
    lista_diccionario.append(ejercicio_nuevo)

    return ejercicio_nuevo
    


if __name__=="__main__":

    print("Bienvenid@ al programa de gestión de ejercicios.\n Estos son los comandos a usar: \n - crear: Crea nuevo ejercicio.\n - listar: Muestra todos los ejercicios. \n - entrenamiento: Genera un entrenamiento con la duración aportada \n - consulta: Consulta todos los ejercicios con la duración aportada. \n - fin: Sale del programa")
    mostrar_input=True
    while mostrar_input:
        comando = input("Introduce un comando: ")

        if comando == "crear":
            print(nuevo_ejercicio(ejercicios))
        elif comando == "listar":
            
            for i in ejercicios:
                listado=[]
                for clave,valor in i.items():
                    listado.append((clave,valor))
                print(f"{listado[0]} ({listado[3]}) \n {listado[1]}")
                for t in i["estrategia"]:
                    print(f"-{t}")    


           
        elif comando == "entrenamiento":
            valido=False
            while not valido:
                minutos=int(input("Introduce un numero multiplo de 10: "))
                if minutos%10 == 0:
                    valido = True
                else: 
                    print("No es un tiempo valido")    
            print(entrenamiento(ejercicios,minutos))
        elif comando == "consulta":
            vale=False
            while not vale:
                mins=int(input("Introduce un numero multiplo de 10: "))
                if mins%10 == 0:
                    vale = True
                else: 
                    print("No es un tiempo valido") 
            print(filtra_ejercicios(ejercicios,mins))
        elif comando == "fin":
            print("Adios")
            mostrar_input = False
        else:
            print("No es un comando valido")


