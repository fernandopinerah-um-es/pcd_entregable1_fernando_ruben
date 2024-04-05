from enum import Enum

class Universidad():
    def __init__(self):
        self.investigadores = []
        self.titulares = []
        self.asociados = []
        self.estudiantes = []

    def altaInvestigador(self, investigador):
        self.investigadores.append(investigador)

    def eliminarInvestigador(self,investigador):
        self.investigadores.remove(investigador)

    def altaTitular(self,titular):
        self.titulares.append(titular)

    def eliminarTitular(self, titular):
        self.titulares.remove(titular)

    def altaAsociado(self,asociado):
        self.asociados.append(asociado)

    def eliminarAsociado(self,asociado):
        self.asociados.remove(asociado)

    def altaEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def eliminarEstudiante(self,estudiante):
        self.estudiantes.remove(estudiante)

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    def devuelveDatos(self):
        return "Nombre: " + self.nombre + ", DNI: " + self.dni + ", Dirección: " + self.direccion + ", Sexo: " + self.sexo
    
class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        Persona.__init__(self, nombre, dni, direccion, sexo)
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        else:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")

class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class Miembro(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        Persona.__init__(self, nombre, dni, direccion, sexo)
        self.departamento = departamento
    
    def cambiarDepartamento(self,departamento):
        self.departamento = departamento

class ProfesorAsociado(Miembro):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        Miembro.__init__(self, nombre, dni, direccion, sexo, departamento)
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        else:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")

class Investigador(Miembro):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area):
        Miembro.__init__(self, nombre, dni, direccion, sexo, departamento)
        self.area = area

    def cambiarArea(self,area):
        self.area = area

    def datos(self):
        return Persona.devuelveDatos(self) +" , Área: "+(self.area)

class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area):
        Investigador.__init__(self, nombre, dni, direccion, sexo, departamento, area)
        self.investigador = True
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        else:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")

    def asignarInvestigador(self,area):
        self.investigador = True
        self.area = area

    def quitarInvestigador(self):
        self.investigador = False
        self.area = None

if __name__ == "__main__":
    # Creamos una instancia de Universidad
    universidad = Universidad()

    # Creamos algunos estudiantes
    estudiante1 = Estudiante("Juan", "12345678A", "Calle Principal 123", "M")
    estudiante2 = Estudiante("María", "98765432B", "Avenida Central 456", "F")

    # Añadimos estudiantes a la universidad
    universidad.altaEstudiante(estudiante1)
    universidad.altaEstudiante(estudiante2)

    # Mostramos los datos de los estudiantes
    print("Datos de los estudiantes:")
    print(estudiante1.devuelveDatos())
    print(estudiante2.devuelveDatos())

    # Añadimos asignaturas a un estudiante
    estudiante1.añadirAsignaturas("Matemáticas")
    estudiante1.añadirAsignaturas("Historia")
    estudiante2.añadirAsignaturas("Física")

    # Mostramos las asignaturas de un estudiante
    print("Asignaturas de los estudiantes:")
    print(estudiante1.listAsignaturas())
    print(estudiante2.listAsignaturas())

    # Eliminamos asignaturas de un estudiante
    estudiante1.eliminarAsignaturas("Historia")

    # Mostramos las asignaturas actualizadas de un estudiante
    print("Asignaturas de los estudiantes después de eliminar Historia:")
    print(estudiante1.listAsignaturas())

    # Creamos algunos profesores asociados
    profesor_asociado1 = ProfesorAsociado("Pedro", "11111111X", "Calle Mayor 789", "M", Departamento.DIIC)
    profesor_asociado2 = ProfesorAsociado("Laura", "22222222Y", "Plaza Central 123", "F", Departamento.DITEC)

    # Añadimos profesores asociados a la universidad
    universidad.altaAsociado(profesor_asociado1)
    universidad.altaAsociado(profesor_asociado2)

    # Cambiamos el departamento de un profesor asociado
    profesor_asociado1.cambiarDepartamento(Departamento.DIS)

    # Mostramos los datos de los profesores asociados
    print("Datos de los profesores asociados:")
    print(profesor_asociado1.devuelveDatos())
    print(profesor_asociado2.devuelveDatos())

    # Creamos un investigador
    investigador1 = Investigador("Carlos", "33333333Z", "Avenida Principal 456", "M", Departamento.DIIC, "Inteligencia Artificial")

    # Añadimos investigador a la universidad
    universidad.altaInvestigador(investigador1)

    # Cambiamos el área de investigación del investigador
    investigador1.cambiarArea("Redes Neuronales")

    # Mostramos los datos del investigador
    print("Datos del investigador:")
    print(investigador1.devuelveDatos())

    # Creamos un profesor titular
    profesor_titular1 = ProfesorTitular("Ana", "44444444W", "Avenida Central 789", "F", Departamento.DITEC, "Machine Learning")

    # Añadimos profesor titular a la universidad
    universidad.altaTitular(profesor_titular1)

    # Asignamos rol de investigador al profesor titular
    profesor_titular1.asignarInvestigador()

    # Mostramos los datos del profesor titular
    print("Datos del profesor titular:")
    print(profesor_titular1.devuelveDatos())