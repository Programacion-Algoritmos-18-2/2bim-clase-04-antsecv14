#Importamos los codecs
import codecs
#Creamos la clase Equipo
class Equipo(object):
	def __init__(self,nom,c,p,j):
		self.nombre = nom
		self.ciudad = c
		self.campeonatos = int(p)
		self.numjugadores = int(j)
#Creamos los get y set de cada variable
	def agregar_nombre(self,nom):
		self.nombre = nom

	def agregar_ciudad(self,c):
		self.apellidos = c

	def agregar_campeonatos(self,p):
		self.edad = int(p)

	def agregar_numjugadores(self,j):
		self.numjugadores = int(j)

	def obtener_nombre(self):
		return self.nombre

	def obtener_ciudad(self):
		return self.ciudad

	def obtener_campeonatos(self):
		return self.campeonatos

	def obtener_numjugadores(self):
		return self.numjugadores
#Creamos el str y el repr
	def __str__(self):
		return "%s %s %d %.2f" %(self.nombre, self.ciudad, self.campeonatos, self.numjugadores)

	def __repr__(self):
		return "%s %s %d %.2f" %(self.nombre, self.ciudad, self.campeonatos, self.numjugadores)
#Creamos la clase MiArchivo
class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()

#Creamos la clase Operaciones para ordenar la lista medienate los metodos ordenar y ordenar2
class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipo = listado
    def ordenar(self):
        return sorted(self.listado_equipo, key=lambda equipo: equipo.obtener_nombre())
    def ordenar2(self):
        return sorted(self.listado_equipo, key=lambda equipo: equipo.obtener_campeonatos())



#Creamos MiArchivoEscribir para poder agregar toda la informacion ordenada en un nuevo archivo
class MiArchivoEscribir:

    def __init__(self):
        self.archivo = codecs.open("data/ordenamiento.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s %s %d %d" %(p.nombre, p.ciudad, p.campeonatos, p.numjugadores))

    def cerrar_archivo(self):
        self.archivo.close()
