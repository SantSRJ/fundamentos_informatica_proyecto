class Empleado:
    def __init__(self, id, nombre, apellido, cargo, correo, telefono, direccion, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Cargo: {self.cargo}, Correo: {self.correo}, Telefono: {self.telefono}, Direccion: {self.direccion}, Salario: {self.salario}"

class ListadoEmpleados:
    def __init__(self):
        self.listado = [
            Empleado(1, "Elena", "González", "Gerente de Ventas", "elenagonzalez@example.com", "1122334455", "Calle Principal 123", 50000),
            Empleado(2, "Mario", "Martínez", "Vendedor", "mariomartinez@example.com", "9988776655", "Avenida Secundaria 456", 30000),
            Empleado(3, "Laura", "Pérez", "Asesor Financiero", "lauraperez@example.com", "5544332211", "Boulevard Comercial 789", 35000),
            Empleado(4, "Diego", "López", "Mecánico", "diegolopez@example.com", "6677889900", "Calle de los Talleres 321", 28000),
            Empleado(5, "Carolina", "Ruiz", "Recepcionista", "carolinaruiz@example.com", "3322114455", "Avenida de Recepción 654", 25000)
        ]

    def agregar_empleado(self, empleado):
        self.listado.append(empleado)

    def buscar_empleado(self, id):
        for empleado in self.listado:
            if empleado.id == id:
                return empleado

    def mostrar_listado(self):
        print("Listado de Empleados:")
        for empleado in self.listado:
            print(empleado)

    def obtener_listado(self):
        return self.listado
'''
listado.agregar_empleado(Empleado(1, "Elena", "González", "Gerente de Ventas", "elenagonzalez@example.com", "1122334455", "Calle Principal 123", 50000))
listado.agregar_empleado(Empleado(2, "Mario", "Martínez", "Vendedor", "mariomartinez@example.com", "9988776655", "Avenida Secundaria 456", 30000))
listado.agregar_empleado(Empleado(3, "Laura", "Pérez", "Asesor Financiero", "lauraperez@example.com", "5544332211", "Boulevard Comercial 789", 35000))
listado.agregar_empleado(Empleado(4, "Diego", "López", "Mecánico", "diegolopez@example.com", "6677889900", "Calle de los Talleres 321", 28000))
listado.agregar_empleado(Empleado(5, "Carolina", "Ruiz", "Recepcionista", "carolinaruiz@example.com", "3322114455", "Avenida de Recepción 654", 25000))
'''