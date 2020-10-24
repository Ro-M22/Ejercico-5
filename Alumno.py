class Alumno:
    cant_max_inasistencias=40
    cantidad_total_clases=250
    contrasenia=12345            #AGREGADO
    __nombreAlumno = ''
    __anio = 0
    __division = 0
    __cantInasitencias = 0
    @classmethod
    def getCant_Max_Asistencia(cls):
        return cls.cant_max_inasistencias
    @classmethod
    def get_cantidad_total_clase(cls):
        return cls.cantidad_total_clases
    @classmethod
    def VerificaContrasenia(cls, passw):
        if passw==cls.contrasenia:
            print("\n\t\t CORRECTO")
            return passw
        else:
                print("\n\t\t CONTRASEÑA INCORRECTA")
    @classmethod
    def actualiza_cant_max_inasistencias(cls, passw, cant):
        if passw==cls.contrasenia:
            cls.cant_max_inasistencias=cant
        else:
            print("\n\t\t No puede cambiar estos datos")

    def __init__(self, nombre='', anio=0, division=0, cantI=0):

        self.__nombreAlumno = nombre
        self.__anio = anio
        self.__division = division
        self.__cantInasitencias = cantI

    def getNombre(self):
        return self.__nombreAlumno

    def getAnio(self):
        return self.__anio

    def getDivision(self):
        return self.__division

    def getCantidadInasistencias(self):
        return self.__cantInasitencias

    def MostrarDatos(self):
        print("{0:2} {1:2} {2:2} {3:2}".format(self.__nombreAlumno, self.__anio, self.__division, self.__cantInasitencias))




###############################PRUEBA DE METODOS CLASE####

#alumno= Alumno("jeremias")
#otroA = Alumno("JOSE", 3, 2, 44)
#print(alumno.getNombre())
#print(alumno.getAnio())
#print(alumno.getDivision())
#print(alumno.getCantidadInasistencias())
#print("CLASE: ", alumno.getCant_Max_Asistencia(), "ALUMNO: ",alumno.getNombre())
#print(otroA.getNombre())
#print(otroA.getAnio())
#print(otroA.getDivision())
#print(otroA.getCantidadInasistencias())
#print("CLASE: ", otroA.getCant_Max_Asistencia(), "ALUMNO: ",otroA.getNombre())

###################################################FIN












