from enum import Enum

class Universidad:
    def __init__(self):
        self.investigadores = []
        self.titulares = []
        self.asociados = []
        self.estudiantes = []

    def altaInvestigador(self, investigador):
        if investigador in self.investigadores:
            print(f"Investigador {investigador.nombre} ya existe.")
            return
        self.investigadores.append(investigador)

    def eliminarInvestigador(self, investigador):
        try:
            self.investigadores.remove(investigador)
        except ValueError:
            raise ValueError("El investigador no está registrado")
        
    def listInvestigadores(self):
        return self.investigadores

    def altaTitular(self, titular):
        if titular in self.titulares:
            print(f"Titular {titular.nombre} ya existe.")
            return
        self.titulares.append(titular)

    def eliminarTitular(self, titular):
        try:
            self.titulares.remove(titular)
        except ValueError:
            raise ValueError("El titular no está registrado")

    def listTitulares(self):
        return self.titulares
    
    def altaAsociado(self, asociado):
        if asociado in self.asociados:
            print(f"Asociado {asociado.nombre} ya existe.")
            return
        self.asociados.append(asociado)

    def eliminarAsociado(self, asociado):
        try:
            self.asociados.remove(asociado)
        except ValueError:
            raise ValueError("El asociado no está registrado")

    def listAsociados(self):
        return self.asociados
    
    def altaEstudiante(self, estudiante):
        if estudiante in self.estudiantes:
            print(f"Estudiante {estudiante.nombre} ya existe.")
            return
        self.estudiantes.append(estudiante)

    def eliminarEstudiante(self, estudiante):
        try:
            self.estudiantes.remove(estudiante)
        except ValueError:
            raise ValueError("El estudiante no está registrado")

    def listEstudiantes(self):
        return self.estudiantes

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        if sexo not in ['V', 'M']:
            raise ValueError("El sexo debe ser 'V' o 'M'.")
        self.sexo = sexo

    def devuelveDatos(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}"


class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        Persona.__init__(self,nombre, dni, direccion, sexo)
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            print(f"Asignatura {asignatura} ya existe en las asignaturas de {self.nombre}.")
            return
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        try:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        except ValueError:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")

class Departamento():
    DIIC = 1
    DITEC = 2
    DIS = 3


class Miembro(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        Persona.__init__(self, nombre, dni, direccion, sexo)
        self.departamento = departamento

    def cambiarDepartamento(self, departamento):
        if departamento != self.departamento:
            self.departamento = departamento
        else:
            print("El miembro ya pertenece a este departamento.")

    def datos(self):
        return f"{Persona.devuelveDatos(self)}, Departamento: {self.departamento}"

class ProfesorAsociado(Miembro):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        Miembro.__init__(self,nombre, dni, direccion, sexo, departamento)
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            print(f"Asignatura {asignatura} ya existe en las asignaturas de {self.nombre}.")
            return
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        try:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        except ValueError:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")


class Investigador(Miembro):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area):
        Miembro.__init__(self,nombre, dni, direccion, sexo, departamento)
        self.area = area

    def cambiarArea(self, area):
        if area != self.area:
            self.area = area
        else:
            print("El miembro ya pertenece a este área.")

    def datos(self):
        return f"{Miembro.datos(self)}, Área: {self.area}"


class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area):
        Investigador.__init__(self,nombre, dni, direccion, sexo, departamento, area)
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            print(f"Asignatura {asignatura} ya existe en las asignaturas de {self.nombre}.")
            return
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        try:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        except ValueError:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")

    def asignarInvestigador(self, area):
        self.investigador = True
        self.area = area

    def quitarInvestigador(self):
        self.investigador = False
        self.area = None

if __name__ == "__main__":
    # Creamos una instancia de la clase Universidad
    mi_universidad = Universidad()

    # Creamos investigadores
    investigador1 = Investigador("Juan", "12345678", "Calle 123", "V", Departamento.DIIC, "Ciencias")
    investigador2 = Investigador("María", "87654321", "Avenida 456", "M", Departamento.DITEC, "Física")

    # Mostramos sus datos
    print(investigador1.devuelveDatos())
    print(investigador2.devuelveDatos())

    # Alta de investigadores en la universidad
    mi_universidad.altaInvestigador(investigador1)
    mi_universidad.altaInvestigador(investigador2)

    # Vemos que se han añadido
    print(mi_universidad.listInvestigadores())

    # Eliminación de un investigador
    mi_universidad.eliminarInvestigador(investigador1)

    # Vemos que se ha eliminado
    print(mi_universidad.listInvestigadores())

    # Creación de un titular
    titular1 = ProfesorTitular("Pedro", "23456789", "Carrera 789", "V", Departamento.DIIC, "Matemáticas")

    # Mostramos sus datos
    print(titular1.datos())

    # Alta de titulares en la universidad
    mi_universidad.altaTitular(titular1)

    # Vemos que se ha añadido
    print(mi_universidad.listTitulares())

    # Eliminación de un titular
    mi_universidad.eliminarTitular(titular1)

    # Vemos que se ha eliminado
    print(mi_universidad.listTitulares())

    # Creación de un asociado
    asociado1 = ProfesorAsociado("Laura", "98765432", "Calle 987", "M", Departamento.DIS)

    # Vemos sus datos
    print(asociado1.datos())

    # Alta de asociados en la universidad
    mi_universidad.altaAsociado(asociado1)

    # Vemos que se ha añadido
    print(mi_universidad.listAsociados())

    # Eliminación de un asociado
    mi_universidad.eliminarAsociado(asociado1)

    # Vemos que se ha eliminado
    print(mi_universidad.listAsociados())

    # Creación de un estudiante
    estudiante1 = Estudiante("Carla", "34567890", "Avenida 456", "M")

    # Vemos sus datos
    print(estudiante1.devuelveDatos())

    # Alta de estudiantes en la universidad
    mi_universidad.altaEstudiante(estudiante1)

    # Vemos que se ha añadido
    print(mi_universidad.listEstudiantes())

    # Eliminación de un estudiante
    mi_universidad.eliminarEstudiante(estudiante1)

    # Vemos que se ha eliminado
    print(mi_universidad.listEstudiantes())

    # Cambio de departamento para un miembro
    titular1.cambiarDepartamento(Departamento.DITEC)

    # Vemos sus datos
    print(titular1.datos())

    # Cambio de área para un investigador
    investigador2.cambiarArea("Química")


    # Añadimos asignaturas para un estudiante
    estudiante1.añadirAsignaturas("Matemáticas")
    estudiante1.añadirAsignaturas("Física")

    # Eliminamos asignaturas para un estudiante
    estudiante1.eliminarAsignaturas("Matemáticas")

    # Obtenemos los datos de un investigador
    print(investigador2.datos())

    # Listamos asignaturas de un estudiante
    print(estudiante1.listAsignaturas())
