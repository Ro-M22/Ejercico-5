from ManejadorAlumno import ManejadorAlumno
from Alumno import Alumno


def zero(alumnoMain,manejadorA):
    print("\t\t\t  >>>>  FIN DEL PROGRAMA  <<<<")

def one(alumnoMain, manejadorA):                       #LISTADO DE ALUMNOS
    print("\t\t\tLISTADO DE ALUMNOS QUE SUPERAN EL MAXIMO\n")
    i=0
    print("\t >> Por favor ingrese los siguientes datos")
    anio=int(input("\t\t + AÑO: "))     #Probar con 6
    div=int(input("\t\t + DIVISION: ")) #Probar con 2
    #band=False
    print("\n\t\tAlumno                    Porcentaje de Inasistencias")
    while i in range(len(manejadorA.getALUMNOS())):
        a=manejadorA.getAnioLista(i)
        b=manejadorA.getDiv(i)
        if a==anio and b==div:
            asistencia=int(manejadorA.getFaltas(i))
            maximofaltas=int(alumnoMain.getCant_Max_Asistencia())
            if int(asistencia)>maximofaltas:
                porcentaj=float((int(asistencia)*100/int(maximofaltas)))
                print("\t%17s\t        \t \t\t\t%3.2f"%(manejadorA.getAlumno(i), porcentaj),"%\t")
                i+=1
            else:
                i+=1
        else:
            i+=1
    x=i
    if x>=i:
            print("\n\t\t\t\t\tFin de Lista")
            input('\n \t--> Presione enter para continuar ')
            print('----------------------------------------------------------------------------------\n')
    print()
    print("\t\t\tLISTADO DE ALUMNOS DEL ARCHIVO\n")
    for i in range(len(manejadorA.getALUMNOS())):
        print(manejadorA.getAlumnoslista(i))
        i+=1
    input('\n \t--> Presione enter para continuar ')
    print('----------------------------------------------------------------------------------\n')

def two(alumnoMain, manejadorA):                       #MODIFICA ATRIBUTO DE CLASE

    print("                    MODIFICAR CANTIDAD MAXIMA DE INASISTENCIAS\n")
    cantidadMaxima = alumnoMain.getCant_Max_Asistencia()
    print("\t\t Cantidad de Inasistencias Maximas Actuales: ", cantidadMaxima)
    print("\n\t \t Ingrese Contraseña Numérica de Seguridad: ") # Agregamos esta opcion para que no cualquiera pueda cambiar las inasistencias >> LA CLAVE ES: 12345 <<
    passw = int(input('\t\t'))
    verificacion= alumnoMain.VerificaContrasenia(passw)
    if passw==verificacion:
         nuevacant = int(input("\n\t\t Ingrese Cantidad Maxima Deseada: "))
         alumnoMain.actualiza_cant_max_inasistencias(passw, nuevacant)

         cantidadMaxima=alumnoMain.getCant_Max_Asistencia()
         print("\t\t Nueva Cantidad de Inasistencias Maximas : ", cantidadMaxima)
         input('\n \t--> Presione enter para continuar ')
         print('\n----------------------------------------------------------------------------------\n')

    else:
        print('\n \t -- NO SE PUEDEN MODIFICAR LOS DATOS --')


switcher = {
    0: zero,
    1: one,
    2: two
}

def switch(argument, alumnoMain, manejadorA):
    func = switcher.get(argument, lambda x,y: print("\t\t\t\t\t\t\t Opción incorrecta\n \n----------------------------------------------------------------------------------\n"))
    func(alumnoMain, manejadorA)

if __name__ == '__main__':
    alumnoMain= Alumno()
    manejadorA= ManejadorAlumno()
    manejadorA.TestAlumnos()
    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print('\t\t#################################################')
        print("\t\t# 0- SALIR                                      #")
        print("\t\t# 1- LISTADO ALUMNOS QUE SUPERAN INASISTENCIAS  #")
        print("\t\t# 2- MODIFICAR CANTIDAD MAXIMA DE INASISTENCIAS #")
        print('\t\t#################################################')
        opcion= int(input("\n\t\t>>Ingrese una opción: "))
        print('\n----------------------------------------------------------------------------------\n')
        switch(opcion, alumnoMain, manejadorA)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú