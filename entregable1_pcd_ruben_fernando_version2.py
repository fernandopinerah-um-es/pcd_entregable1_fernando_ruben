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