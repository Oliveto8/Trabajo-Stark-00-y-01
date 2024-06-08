
def menu()->str:
  #limpiar_pantalla()
  print(f"{'\n--Menu de opciones--\n'}")
  print("1- nombre de cada superhéroe de género M")
  print("2- nombre de cada superhéroe de género F")
  print("3- superhéroe más alto de género M")
  print("4- superhéroe más alto de género F")
  print("5- superhéroe más bajo de género M")
  print("6- superhéroe más bajo de género F")
  print("7- promedio de los superhéroes de género M")
  print("8- promedio de los superhéroes de género F")
  print("9- Listar todos los superhéroes agrupados por color de ojos")
  print("10- Listar todos los superhéroes agrupados por color de pelo")
  print("11- Listar todos los superhéroes agrupados por el tipo de inteligencia")
  print("12- Salir")
  return input(f"\ningrese una opcion: ")

def pausar():
  import os
  print("")
  os.system("pause")
  

def limpiar_pantalla():
  import os
  os.system("cls")

def pedir_confirmacion(mensaje:str)->bool:
  rta = input(mensaje).lower()
  return rta == 'si'

