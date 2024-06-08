from funciones_menu import *
from funciones import *
from data_stark import lista_personajes

""" Desafío #01:
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia """

seguir = "si"

for heroe in lista_personajes:
    heroe['altura'] = float(heroe['altura'])
    heroe['peso'] = float(heroe['peso'])
    heroe['fuerza'] = int(heroe['fuerza'])

while seguir == "si":
  match menu():
    case "1":
      lista_genero_masculino = fitrar_lista_segun_dato(lista_personajes,"genero","M")
      imprimir_lista_nombres(lista_genero_masculino)
    case "2":
      lista_genero_femenino = fitrar_lista_segun_dato(lista_personajes,"genero","F")
      imprimir_lista_nombres(lista_genero_femenino)
    case "3":
      lista_genero_masculino = fitrar_lista_segun_dato(lista_personajes, "genero", "M")
      nombre_mas_alto_masculino = determinar_maximo_minimo_dato(lista_genero_masculino, "altura",True)
      print("\nEl superheroe más alto es:", nombre_mas_alto_masculino)
    case "4":
      lista_genero_femenino = fitrar_lista_segun_dato(lista_personajes, "genero", "F")
      nombre_mas_alto_femenino = determinar_maximo_minimo_dato(lista_genero_femenino, "altura",True)
      print("\nLa superheroina más alta es:", nombre_mas_alto_femenino)
    case "5":
      lista_genero_masculino = fitrar_lista_segun_dato(lista_personajes, "genero", "M")
      nombre_mas_bajo_masculino = determinar_maximo_minimo_dato(lista_genero_masculino, "altura",False)
      print("\nEl superheroe más bajo es:", nombre_mas_bajo_masculino)
    case "6":
      lista_genero_femenino = fitrar_lista_segun_dato(lista_personajes, "genero", "F")
      nombre_mas_bajo_femenino = determinar_maximo_minimo_dato(lista_genero_femenino, "altura",False)
      print("\nLa superheroina más baja es:", nombre_mas_bajo_femenino)
    case "7":
      superheroes_masculinos = fitrar_lista_segun_dato(lista_personajes, 'genero', 'M')
      altura_promedio_masculinos = calcular_promedio_dato(superheroes_masculinos, 'altura')
      print(f"\nAltura promedio de superheroes de genero masculino: {altura_promedio_masculinos:.2f}")
    case "8":
      superheroes_femeninos = fitrar_lista_segun_dato(lista_personajes, 'genero', 'F')
      altura_promedio_femeninos = calcular_promedio_dato(superheroes_femeninos, 'altura')
      print(f"\nAltura promedio de superheroes de genero femenino: {altura_promedio_femeninos:.2f}")
    case "9":
      lista_colores_ojos = listar_dato_y_sus_valores(lista_personajes,"color_ojos")
      mostrar_dato_y_lista(lista_colores_ojos)
    case "10":
      lista_colores_pelo = listar_dato_y_sus_valores(lista_personajes,"color_pelo")
      mostrar_dato_y_lista(lista_colores_pelo,"ojos")
    case "11":
      lista_tipo_inteligencia = listar_dato_y_sus_valores(lista_personajes,"inteligencia")
      mostrar_dato_y_lista(lista_tipo_inteligencia,"inteligencia")
    case "12":
      if pedir_confirmacion("\n¿Confirmar salida? "):
        seguir = "no"
        continue
    case _:
      print("\nIngrese uno de los numneros indicados")
  pausar()

print("\nFin del programa")