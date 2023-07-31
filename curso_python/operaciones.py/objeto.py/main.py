
objeto={}
objeto['nombre']= input ('Ingrese su nombre: ' )
objeto['edad']=int(input('Ingrese su edad: ' ))
objeto['telefono']=int(input ('Ingrese numero de telefono: ' ))
objeto['correp']= input('Ingrese su correo electronico: ' )

print ( objeto)








# 
# crear una lista para crear dos objetos en una lista 

# Lista=[]
# while len(Lista)<=1:
#     objeto={}
#     objeto['nombre']=input('Nombre de mascota: ' )
#     objeto['Edad']=int(input('edad de mascota: ' ))
#     objeto['Croqueta']=input('Coqueta faborita: ' )
#     Lista.append(objeto)
# print(Lista)
    





#ejercicio  2

# Lista=[]
# while True:
#     objeto={}
#     objeto['nombre']=input('Nombre de mascota: ' )
#     objeto['Edad']=int(input('edad de mascota: ' ))
#     objeto['Croqueta']=input('Coqueta faborita: ' )
#     Lista.append(objeto)
#     condicion=input( 'si desea salir escriba escriba: S , si desea continuar : C  ' )
#     if condicion.upper()== 'S':
#         break
   
# print(Lista)


##lower→ }



Lista=[]
while True:
    objeto={}
    objeto['nombre']=input('Nombre de mascota: ' )
    objeto['Edad']=int(input('edad de mascota: ' ))
    
    objeto ['comidas']=[]
    while len(objeto['comidas'])<3:
        comida=input('Ingrese la comida faborita: ' )
        objeto['comidas'] .append(comida)
    Lista.append(objeto)
    condicion=input( 'si desea salir escriba escriba: S , si desea continuar : C  ' )
    if condicion.upper()== 'S':
        break
   
print(Lista)




empresa ={}
empresa['nombre']=input('ingrese nombre de la empresa : ')
empresa['ruc']=int(input('ingrese ruc de la empresa : '))
empresa['direccion']=(input('ingrese direccion a la empresa : '))
empresa['sucursales']=[]
while len(empresa['sucursales']) <2 :
  sucursal = input('ingrese el nombre de la sucursal : ')
  empresa ['sucursales'].append(sucursal)
  empresa['horario']={}
  empresa['horario']['dia'] = input('ingrese el horario del dia : ')
  empresa['horario']['tarde']=input('ingrese el horario de la tarde : ')
print(empresa)




#ejercicio 2


empresa=input('Ingrese el nombre de la empresa: ' )
ruc=input('Ingrese numero de ruc: ' )
direccion=input('Ingrese direccion: ' )
sucursales=[]
for indice in range(0,3):
  sucursal=input('Ingrese la sucursal: ' )
  sucursal.append(sucursal )
empresa={'nombre':empresa,
         'ruc':ruc,
         'direccion':direccion,
         'horario':horario
         
         }  



# ejercicio 3

nombre=input('ingrese el nombre de la empresa: ' )
ruc=input('Ingrese numero de ruc: ' )
direccion=input('Ingrese direccion: ' )
sucursales=input('ingrse las sucursales separado por comas: ' ).split(',')
horario_dia=input('ingrese el horario de dia: ' )
horario_tarde=input('ingrese el horario de tarde: ' )

empresa={'nombre':nombre,
         'ruc':ruc,
         'direccion':direccion,
         'sucursal': sucursales,
         'horario':{
           'dia':horario_dia,
           'noche':horario_tarde
         }  
}
print(empresa)

    
    