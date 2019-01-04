from modelado.archivo import *

m = MiArchivo() 

#m2 = MiArchivoEscribir() 

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

lista_obj = []

for d in lista:
	p = Equipo(d[0],d[1],d[2],d[3])

operacion = Operaciones(lista)

print(operacion.ordenar())

print(operacion.ordenar2())

#ordenamiento = input("Desea ordenar por : nombre(1) \n\t\t\tcampeonato(2)\n")


#if (ordenamiento == 1):

	

