
def menu()->str:
  #limpiar_pantalla()
  print(f"{'\n--Menu de opciones--\n'}")
  print("1- Mostrar los nombres de los heroes")
  print("2- mostrar nombres y alturas de los heroes")
  print("3- mostrar cual es el heroe con mayor y menor altura")
  print("4- mostrar cual es el heroe con mayor y menor peso")
  print("5- Salir")
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

