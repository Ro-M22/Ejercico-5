import csv
from Alumno import Alumno

class ManejadorAlumno:
    #__lista = []

    def __init__(self, ):
        self.__listaAlumnos = []

    def agregarAlumno(self, unalumno):
        self.__listaAlumnos.append(unalumno)

    def getALUMNOS(self):
        return self.__listaAlumnos

    def getAlumnoslista(self,unAlumno):
        return self.__listaAlumnos[unAlumno].MostrarDatos()

    def getAlumno(self,unAlumno):
        return self.__listaAlumnos[unAlumno].getNombre()

    def getAnioLista(self, unAlumno):
        return self.__listaAlumnos[unAlumno].getAnio()

    def getDiv(self, unAlumno):
        return self.__listaAlumnos[unAlumno].getDivision()

    def getFaltas(self, unAlumno):
        return self.__listaAlumnos[unAlumno].getCantidadInasistencias()

    def __str__(self):
        s = ""
        for alumno in self.__listaAlumnos:
            s+= str(alumno) + '\n'
        return s

    def TestAlumnos(self):
        archivo = open('Alumnos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            nom = fila[0]
            anio = int(fila[1])
            division= int(fila[2])
            inasistencias= int(fila[3])
            unAlumno= Alumno(nom, anio,division, inasistencias)
            #print ("ALUMNO: {} AÑO: {} DIV: {} \n FALTAS: {}\n".format(nom, anio, division, inasistencias))
            self.agregarAlumno(unAlumno)


