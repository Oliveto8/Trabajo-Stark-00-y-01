from funciones_menu import *
from funciones import *
from data_stark import lista_personajes

"""Desafío #00:

A. Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener"""

seguir = "si"

for heroe in lista_personajes:
    heroe['altura'] = float(heroe['altura'])
    heroe['peso'] = float(heroe['peso'])
    heroe['fuerza'] = int(heroe['fuerza'])

while seguir == "si":
  match menu():
    case "1":
      print("")
      mostrar_dato(lista_personajes, "nombre")
    case "2":
      print("\nNombre                Altura")
      mostrar_heroe_dato(lista_personajes,"nombre","altura")
    case "3":
      heroe_mas_alto = determinar_maximo_minimo_dato(lista_personajes,"altura",True)
      heroe_mas_bajo = determinar_maximo_minimo_dato(lista_personajes,"altura",False)
      promedio_altura = calcular_promedio_dato(lista_personajes,"altura")
      print(f"\nEl heroe mas alto es: {heroe_mas_alto}, el mas bajo es: {heroe_mas_bajo} y el promedio de altura es de: {promedio_altura:0.2f}")
    case "4":
      heroe_mas_pesado = determinar_maximo_minimo_dato(lista_personajes,"peso",True)
      heroe_menos_pesado = determinar_maximo_minimo_dato(lista_personajes,"peso",False)
      print(f"\nEl heroe mas pesado es: {heroe_mas_pesado} y el menos pesado es: {heroe_menos_pesado}")
    case "5":
      if pedir_confirmacion("\n¿Confirmar salida? "):
        seguir = "no"
        continue
    case _:
      print("\nIngrese uno de los numneros indicados")
  pausar()

print("\nFin del programa")