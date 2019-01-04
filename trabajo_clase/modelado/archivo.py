
import codecs

class Equipo(object):
	def __init__(self,n,c,p,j):
		self.nombres = n
		self.ciudad = c
		self.campeonatos = int(p)
		self.numjugadores = j

	def agregar_nombres(self,n):
		self.nombres = n

	def agregar_ciudad(self,c):
		self.apellidos = a

	def agregar_campeonatos(self,p):
		self.edad = e

	def agregar_numjugadores(self,j):
		self.numjugadores = p

	def obtener_nombres(self):
		return self.nombres

	def obtener_ciudad(self):
		return self.ciudad

	def obtener_campeonatos(self):
		return self.campeonatos

	def obtener_numjugadores(self):
		return self.numjugadores

	def __str__(self):
		return "%s %s %d %.2f" %(self.nombres, self.ciudad, self.campeonatos, self.numjugadores)

	def __repr__(self):
		return "%s %s %d %.2f" %(self.nombres, self.ciudad, self.campeonatos, self.numjugadores)

class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipo = listado

    def ordenar(self):
        return sorted(self.listado_equipo, key=lambda equipo: equipo.nombres)

    def ordenar2(self):
        return sorted(self.listado_equipo, key=lambda equipo: equipo.campeonatos)


"""

class MiArchivoEscribir:

    def __init__(self):
        self.archivo = codecs.open("data/ordenamiento.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write(self.ordenar())

    def cerrar_archivo(self):
        self.archivo.close()
"""