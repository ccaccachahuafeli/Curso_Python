# operadores con numeros 
# operadores de comparación 
com=12<13 # menor
com=15>14 # mayor
com=12==12 # igual
com=12!=10 # distinto
## operaciones lógicas 
var=False & False
opera=False | True
# operacion aritmetica
op=45|23|5*2
print(opera) 
## asignación aumentada
a=10 
a+=10 ## a=a+10
suma=True +20
print(suma)
suma=False *20
print(suma)
## true == 1
## false ==0
# operaciones con STRING
# combinación de cadenas (concatenación)
letra='hola'+'a todos'
print(letra)
# repetir cadenas
cadena="hola"+5
print(cadena)
# obtener una cadena en especifico
obtenerCadena="hola"
mensaje="ksjfurjjvuj"
#python asigna una cadena de dos tipos de índices 
#índice positivo que de izquierda a derecha impieza de 0
# índice negativo es de derecha a izquierda impieza de -1
# quiero imprimir la letra L de mi variable obtrnerCadena
print(obtenerCadena[-3])
print(mensaje[2]) 
# troceado de cadena 
trocear='un mensaje'
print(trocear[2:])
print(trocear[3:6])
print(trocear[:-3])
# [inicio:final+1]
#[inicio:inicionegativo :-5]

ultimoString="texto largo"
ejemplo="123458"
len=(ejemplo)
# len== te muestra caracteres en numeros
# índice = 5
# longitud= 6
longitud=len(ultimoString)
print(ultimoString[longitud-1])
# pertenencia
pertenencia='hola'in 'hola mundo'
print(pertenencia)
con='a'< 'A' ## codigo ascci