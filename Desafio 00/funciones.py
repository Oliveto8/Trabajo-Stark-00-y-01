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






