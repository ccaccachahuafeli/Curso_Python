# EJERCICIO UNO
# escriba una programa que acepte el radio de un circulo  y 
# complete su area 



# hacer un programa que pida al usuario su DNI si la longitud  del DNI es 8 que pida 
##su nombre y lo muestre en consola si la longitud del DNI es mayor o menor a 8 que muestre
 #un mensaje de de error.
# datos de entrada.
dniUsuario=input("ingrese su dni")
longitudDni=len(dniUsuario)
# proceso
if longitudDni==8:
# entrada
  nombre=input("ingrese su nombre")
  mensaje=f"""hola bienvenido,{nombre}"""
  print(mensaje)
else:
  print("el DNI ingresado es incorrecto")


  ## hacer un programa que pida al usuario su primer apellidos si su apellido 
  ## tiene como ultimos caracteres las letras --ez--  mostrar un mensaje que diga eres 
  ## case español si los caracteres finales son --es-- que diga eres casi peruano.

# datos de entrada
apellido=input("ingrese su apellido")
if apellido[-2:]=='ez':
  print("eres case español")
if apellido[-2:]=='es':
   print("eres case peruano")
