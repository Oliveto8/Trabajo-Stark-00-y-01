from data_stark import lista_personajes

def mostrar_dato(lista: list, dato:str) -> None:
  for heroe in lista:
    print(heroe[dato])

def mostrar_heroe_dato(lista: list, dato1:str, dato2:float) -> None:
  for heroe in lista:
    print(f"{heroe[dato1]:<20} - {heroe[dato2]:0.2f}")

def determinar_maximo_minimo(lista: list, dato: str, value=True) -> float:
  extremo = lista[0][dato]
  for heroe in lista:
    if value:
      if heroe[dato] > extremo:
        extremo = heroe[dato]
    else:
      if heroe[dato] < extremo:
        extremo = heroe[dato]
  return extremo

def determinar_maximo_minimo_dato(lista: list, dato: str, value=True) -> str:
  extremo = determinar_maximo_minimo(lista, dato, value)

  for heroe in lista:
    if heroe[dato] == extremo:
      return heroe['nombre']
    
def calcular_promedio_dato(lista:list, dato:str) -> float:
  acumulador_dato = 0
  for i in lista:
    acumulador_dato = acumulador_dato + i[dato]

  promedio_dato = acumulador_dato / len(lista)
  return promedio_dato


def imprimir_lista_nombres(lista:list) -> None:
  for i in lista:
    print(i["nombre"])

def fitrar_lista_segun_dato(lista:list, dato:str, valor:str):
  lista_segun_dato = []
  for personaje in lista:
    if personaje[dato] == valor:
      lista_segun_dato.append(personaje)
  return lista_segun_dato

def listar_dato_y_sus_valores(lista:list,dato:str):
  datos_con_valores = {}

  for personajes in lista:
    dato_y_valor = personajes[dato]
    if dato_y_valor not in datos_con_valores:
      datos_con_valores[dato_y_valor] = []
    datos_con_valores[dato_y_valor].append(personajes)
  return datos_con_valores

def mostrar_dato_y_lista(lista:list,clave:str):
  for dato in lista:
    cantidad = len(lista[dato])
    if dato != "":
        print(f"\nHay {cantidad} superheroes con el tipo de {clave} - {dato}")
    else:
      print(f"\nNo tiene {clave}")
    for personajes in lista[dato]:
      print(f"-{personajes['nombre']}")



