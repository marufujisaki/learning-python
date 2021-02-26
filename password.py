import re

def contador(entrada):
  result = len(entrada)
  if result < 8 or result > 12:
    return False
    print("fallo cantidad")
  else:
    return True

def caracteres(entrada):
  if re.search("[a-z]", entrada) and re.search("[A-Z]", entrada) and re.search("[0-9]", entrada):
    return False
    print("fallo carac")
  else:
    return True

def comienzo(entrada):
  if entrada.startswith("1") or entrada.startswith("A") or entrada.startswith("a"):
    return False
    print("fallo comienzo")
  else:
    return True

def espacio(entrada):
  if re.search("\s", entrada):
    return False
    print("fallo espacio")
  else:
    return True

def confirmacion(entrada):
  confirm = input("Vuelva a ingresar la contraseña: ")
  if entrada == confirm:
    return True
  else:
    return False

def validar(password):
  confirmo = confirmacion(password)
  cont = contador(password)
  com = comienzo(password)
  esp = espacio(password)
  carac = caracteres(password)
  if cont and com and esp and confirmo and carac:
    return True
  else:
    return "La contraseña elegida no es segura"

print(validar("ER2we0BI1to7"))