class Cliente:
    def __init__(self, id, nombre, apellido, telefono, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Teléfono: {self.telefono}, Correo: {self.correo}"

class ListadoClientes:
    def __init__(self):
        self.listado = [
            Cliente(1, "Juan", "Perez", "123456789", "juan@example.com"),
            Cliente(2, "María", "González", "987654321", "maria@example.com"),
            Cliente(3, "Pedro", "Rodríguez", "456789123", "pedro@example.com"),
            Cliente(4, "Ana", "Martínez", "321654987", "ana@example.com"),
            Cliente(5, "Luis", "López", "654987321", "luis@example.com"),
            Cliente(6, "Laura", "Sánchez", "789123456", "laura@example.com"),
            Cliente(7, "Carlos", "García", "456123789", "carlos@example.com"),
            Cliente(8, "Sofía", "Díaz", "987321654", "sofia@example.com"),
            Cliente(9, "Diego", "Hernández", "321789456", "diego@example.com"),
            Cliente(10, "Valentina", "Torres", "654321987", "valentina@example.com")
        ]

    def agregar_cliente(self, cliente):
        self.listado.append(cliente)

    def buscar_cliente(self, id):
        for cliente in self.listado:
            if cliente.id == id:
                return cliente
        return None

    def mostrar_listado(self):
        print("*** Listado de Clientes ***")

        for cliente in self.listado:
            print(cliente)

    def obtener_listado(self):
        return self.listado




'''
# Crear lista de clientes
listado.agregar_cliente(Cliente(1, "Juan", "Perez", "123456789", "juan@example.com"))
listado.agregar_cliente(Cliente(2, "María", "González", "987654321", "maria@example.com"))
listado.agregar_cliente(Cliente(3, "Pedro", "Rodríguez", "456789123", "pedro@example.com"))
listado.agregar_cliente(Cliente(4, "Ana", "Martínez", "321654987", "ana@example.com"))
listado.agregar_cliente(Cliente(5, "Luis", "López", "654987321", "luis@example.com"))
listado.agregar_cliente(Cliente(6, "Laura", "Sánchez", "789123456", "laura@example.com"))
listado.agregar_cliente(Cliente(7, "Carlos", "García", "456123789", "carlos@example.com"))
listado.agregar_cliente(Cliente(8, "Sofía", "Díaz", "987321654", "sofia@example.com"))
listado.agregar_cliente(Cliente(9, "Diego", "Hernández", "321789456", "diego@example.com"))
listado.agregar_cliente(Cliente(10, "Valentina", "Torres", "654321987", "valentina@example.com"))
'''
