


Lista=['texto',10, False ]
#El objeto tranbjan con clave y valor

objeto={'alumno':'jory','edad': 50, 'amigos':['mirella','antony']}

objeto ['alumno']= 'moises'
objeto ['edad']= '25'
objeto ['sexo']= 'todos los dias'
lista=[{'nombre':'jory'},{'nombre'} ,{'moises'},{'nombre:edwin'}]
for indice,list in enumerate(lista):
    print(indice)



  #hacer un programa en python que pida al usuario un texto,
#y evaluar con una funcion la cantidad de vocales'a' que tiene el texto



texto = input("Usted ingrese su  texto  de identificacion: ")

def contar_vocales_a (texto):
    contador = 0
    for letra in texto:
        if letra.lower() == 'a':
            contador += 1
    return contador
cantidad_vocales_a = contar_vocales_a (texto)
print("El TOTAL DE VOCALES A ES :", cantidad_vocales_a, "VOCALES 'a'.")


