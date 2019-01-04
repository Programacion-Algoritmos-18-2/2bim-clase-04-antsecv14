#Importamos todas las clases del archivo archivo.py
from modelado.archivo import *

#Creamos los objetos de la clase MiArchivo y MiArchivoEscribit
m = MiArchivo() 

m2 = MiArchivoEscribir() 

#Creamos una lista para obtener la informacion del archivo mediante nuestro objeto
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
#Creamos lista2 para almacenar las listas ordenadas, y la lista_obj para almacenar los datos del archivo
lista2 = []
lista_obj = []

#Mediante nuestro for agregamos la informacion a la lista_obj
for d in lista:
	p = Equipo(d[0],d[1],d[2],d[3])
	lista_obj.append(p)
#Creamos un objeto tipo operacion y le enviamos lista_obj
operacion = Operaciones(lista_obj)

#Solicitamos al usuario que ingrese el metodo de ordenamiento que desee
opc = int(input("Desea ordenar los equpos por : nombre(1) o por campeonato(2)\n"))

# dependiendo de la opcion la lista1 tomara el ordenamiento respectivo
if opc == 1:
	lista2 = operacion.ordenar()

elif opc == 2:
	lista2 = operacion.ordenar2()

#Se agrega cada elemento de la lista 2 al metodo agregar informacion para escribir el archivo
for d in lista2:
	m2.agregar_informacion(d)
print(lista2)

print("--Proceso realizado con exito--")


	

