class Repuesto:
    def __init__(self,id, marca, nombre, vehiculo, cantidad_stock, precio):
        self.id = id
        self.marca = marca
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.cantidad_stock = cantidad_stock
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Marca: {self.marca}, Nombre: {self.nombre}, Vehiculo: {self.vehiculo}, Cantidad en stock: {self.cantidad_stock}, Precio: {self.precio}"

class ListadoRepuestos:
    def __init__(self):
        self.listado = [
            Repuesto(1, "Bosch", "Filtro de aceite", "Universal", 100, 15.99),
            Repuesto(2, "Fram", "Filtro de aire", "Universal", 120, 12.50),
            Repuesto(3, "Bosch", "Filtro de combustible", "Universal", 90, 20.75),
            Repuesto(4, "Varta", "Batería", "Universal", 50, 89.99),
            Repuesto(5, "Gates", "Bomba de agua", "Universal", 80, 45.25),
            Repuesto(6, "Continental", "Correa de distribución", "Universal", 60, 32.99),
            Repuesto(7, "Bosch", "Bomba de combustible", "Universal", 75, 55.00),
            Repuesto(8, "Denso", "Alternador", "Universal", 40, 120.50),
            Repuesto(9, "Bosch", "Motor de arranque", "Universal", 35, 99.99),
            Repuesto(10, "Bosch", "Sensor de oxígeno", "Universal", 85, 75.25),
            Repuesto(11, "Delphi", "Sensor de temperatura del motor", "Universal", 70, 29.99),
            Repuesto(12, "Valeo", "Radiador", "Universal", 55, 110.75),
            Repuesto(13, "Gates", "Termostato", "Universal", 45, 18.50),
            Repuesto(14, "Luk", "Embrague", "Universal", 30, 180.00),
            Repuesto(15, "Valeo", "Kit de embrague", "Universal", 25, 280.00),
            Repuesto(16, "Brembo", "Disco de freno", "Universal", 110, 45.99),
            Repuesto(17, "Brembo", "Pastillas de freno", "Universal", 105, 35.50),
            Repuesto(18, "Bosch", "Bomba de freno", "Universal", 65, 75.00),
            Repuesto(19, "Bosch", "Cilindro maestro de freno", "Universal", 55, 120.00),
            Repuesto(20, "Bosch", "Cilindro de rueda", "Universal", 50, 45.75),
            Repuesto(21, "Brembo", "Manguera de freno", "Universal", 70, 15.99),
            Repuesto(22, "TRW", "Bomba de dirección asistida", "Universal", 40, 85.50),
            Repuesto(23, "Bosch", "Manguera de dirección asistida", "Universal", 45, 22.75),
            Repuesto(24, "Febi Bilstein", "Soporte de motor", "Universal", 35, 40.00),
            Repuesto(25, "Sachs", "Amortiguador", "Universal", 100, 75.99),
            Repuesto(26, "Monroe", "Resortes", "Universal", 90, 40.25),
            Repuesto(27, "Sachs", "Palanca de cambios", "Universal", 55, 65.50),
            Repuesto(28, "Denso", "Bomba de combustible", "Universal", 80, 110.99),
            Repuesto(29, "Bosch", "Filtro de gasolina", "Universal", 95, 25.75),
            Repuesto(30, "VDO", "Tanque de combustible", "Universal", 60, 185.00),
            Repuesto(31, "GKN", "Eje de transmisión", "Universal", 45, 150.75),
            Repuesto(32, "Bosch", "Kit de reparación de motor", "Universal", 25, 240.00),
            Repuesto(33, "Elring", "Juego de juntas", "Universal", 40, 55.99),
            Repuesto(34, "Gates", "Kit de distribución", "Universal", 30, 120.50),
            Repuesto(35, "NGK", "Bujías de encendido", "Universal", 100, 8.99),
            Repuesto(36, "Bosch", "Cable de bujía", "Universal", 80, 5.50),
            Repuesto(37, "Denso", "Bobina de encendido", "Universal", 70, 35.75),
            Repuesto(38, "Nissens", "Radiador de aceite", "Universal", 55, 75.99),
            Repuesto(39, "Gates", "Mangueras de refrigeración", "Universal", 60, 22.50),
            Repuesto(40, "Bosch", "Bomba de aceite", "Universal", 50, 85.25),
            Repuesto(41, "Victor Reinz", "Juego de juntas de culata", "Universal", 45, 120.00),
            Repuesto(42, "INA", "Tensor de correa de distribución", "Universal", 35, 40.75),
            Repuesto(43, "Febi Bilstein", "Polea de cigüeñal", "Universal", 30, 28.99),
            Repuesto(44, "GKN", "Junta homocinética", "Universal", 25, 65.50),
            Repuesto(45, "Lemförder", "Soportes de transmisión", "Universal", 20, 55.75),
            Repuesto(46, "TRW", "Rótulas de suspensión", "Universal", 40, 18.99),
            Repuesto(47, "Powerflex", "Bujes de suspensión", "Universal", 35, 10.50),
            Repuesto(48, "SKF", "Rodamientos de rueda", "Universal", 60, 45.25),
            Repuesto(49, "Brembo", "Kit de freno de tambor", "Universal", 40, 90.99),
            Repuesto(50, "Bosch", "Kit de reparación de frenos antibloqueo (ABS)", "Universal", 30, 120.75)
        ]

    def agregar_repuesto(self, repuesto):
        self.listado.append(repuesto)

    def buscar_repuesto_id(self, id):
        for repuesto in self.listado:
            if repuesto.id == id:
                return repuesto
        return None

    def buscar_repuesto_nombre(self, nombre):
        lista_nombre = []
        for repuesto in self.listado:
            if repuesto.nombre.lower() == nombre.lower():
                lista_nombre.append(repuesto)

        return lista_nombre

    def mostrar_listado(self):
        print("Listado de Repuestos disponibles:")
        for repuesto in self.listado:
            print(repuesto)

    def obtener_listado(self):
        return self.listado


'''
listado.agregar_repuesto(Repuesto(1, "Bosch", "Filtro de aceite", "Universal", 100, 15.99))
listado.agregar_repuesto(Repuesto(2, "Fram", "Filtro de aire", "Universal", 120, 12.50)),
listado.agregar_repuesto(Repuesto(3, "Bosch", "Filtro de combustible", "Universal", 90, 20.75))
listado.agregar_repuesto(Repuesto(4, "Varta", "Batería", "Universal", 50, 89.99))
listado.agregar_repuesto(Repuesto(5, "Gates", "Bomba de agua", "Universal", 80, 45.25))
listado.agregar_repuesto(Repuesto(6, "Continental", "Correa de distribución", "Universal", 60, 32.99))
listado.agregar_repuesto(Repuesto(7, "Bosch", "Bomba de combustible", "Universal", 75, 55.00))
listado.agregar_repuesto(Repuesto(8, "Denso", "Alternador", "Universal", 40, 120.50))
listado.agregar_repuesto(Repuesto(9, "Bosch", "Motor de arranque", "Universal", 35, 99.99))
listado.agregar_repuesto(Repuesto(10, "Bosch", "Sensor de oxígeno", "Universal", 85, 75.25))
listado.agregar_repuesto(Repuesto(11, "Delphi", "Sensor de temperatura del motor", "Universal", 70, 29.99))
listado.agregar_repuesto(Repuesto(12, "Valeo", "Radiador", "Universal", 55, 110.75))
listado.agregar_repuesto(Repuesto(13, "Gates", "Termostato", "Universal", 45, 18.50))
listado.agregar_repuesto(Repuesto(14, "Luk", "Embrague", "Universal", 30, 180.00))
listado.agregar_repuesto(Repuesto(15, "Valeo", "Kit de embrague", "Universal", 25, 280.00))
listado.agregar_repuesto(Repuesto(16, "Brembo", "Disco de freno", "Universal", 110, 45.99))
listado.agregar_repuesto(Repuesto(17, "Brembo", "Pastillas de freno", "Universal", 105, 35.50))
listado.agregar_repuesto(Repuesto(18, "Bosch", "Bomba de freno", "Universal", 65, 75.00))
listado.agregar_repuesto(Repuesto(19, "Bosch", "Cilindro maestro de freno", "Universal", 55, 120.00))
listado.agregar_repuesto(Repuesto(20, "Bosch", "Cilindro de rueda", "Universal", 50, 45.75))
listado.agregar_repuesto(Repuesto(21, "Brembo", "Manguera de freno", "Universal", 70, 15.99))
listado.agregar_repuesto(Repuesto(22, "TRW", "Bomba de dirección asistida", "Universal", 40, 85.50))
listado.agregar_repuesto(Repuesto(23, "Bosch", "Manguera de dirección asistida", "Universal", 45, 22.75))
listado.agregar_repuesto(Repuesto(24, "Febi Bilstein", "Soporte de motor", "Universal", 35, 40.00))
listado.agregar_repuesto(Repuesto(25, "Sachs", "Amortiguador", "Universal", 100, 75.99))
listado.agregar_repuesto(Repuesto(26, "Monroe", "Resortes", "Universal", 90, 40.25))
listado.agregar_repuesto(Repuesto(27, "Sachs", "Palanca de cambios", "Universal", 55, 65.50))
listado.agregar_repuesto(Repuesto(28, "Denso", "Bomba de combustible", "Universal", 80, 110.99))
listado.agregar_repuesto(Repuesto(29, "Bosch", "Filtro de gasolina", "Universal", 95, 25.75))
listado.agregar_repuesto(Repuesto(30, "VDO", "Tanque de combustible", "Universal", 60, 185.00))
listado.agregar_repuesto(Repuesto(31, "GKN", "Eje de transmisión", "Universal", 45, 150.75))
listado.agregar_repuesto(Repuesto(32, "Bosch", "Kit de reparación de motor", "Universal", 25, 240.00))
listado.agregar_repuesto(Repuesto(33, "Elring", "Juego de juntas", "Universal", 40, 55.99))
listado.agregar_repuesto(Repuesto(34, "Gates", "Kit de distribución", "Universal", 30, 120.50))
listado.agregar_repuesto(Repuesto(35, "NGK", "Bujías de encendido", "Universal", 100, 8.99))
listado.agregar_repuesto(Repuesto(36, "Bosch", "Cable de bujía", "Universal", 80, 5.50))
listado.agregar_repuesto(Repuesto(37, "Denso", "Bobina de encendido", "Universal", 70, 35.75))
listado.agregar_repuesto(Repuesto(38, "Nissens", "Radiador de aceite", "Universal", 55, 75.99))
listado.agregar_repuesto(Repuesto(39, "Gates", "Mangueras de refrigeración", "Universal", 60, 22.50))
listado.agregar_repuesto(Repuesto(40, "Bosch", "Bomba de aceite", "Universal", 50, 85.25))
listado.agregar_repuesto(Repuesto(41, "Victor Reinz",  "Juego de juntas de culata", "Universal", 45, 120.00))
listado.agregar_repuesto(Repuesto(42, "INA", "Tensor de correa de distribución", "Universal", 35, 40.75))
listado.agregar_repuesto(Repuesto(43, "Febi Bilstein", "Polea de cigüeñal", "Universal", 30, 28.99))
listado.agregar_repuesto(Repuesto(44, "GKN", "Junta homocinética", "Universal", 25, 65.50))
listado.agregar_repuesto(Repuesto(45, "Lemförder", "Soportes de transmisión", "Universal", 20, 55.75))
listado.agregar_repuesto(Repuesto(46, "TRW", "Rótulas de suspensión", "Universal", 40, 18.99))
listado.agregar_repuesto(Repuesto(47, "Powerflex", "Bujes de suspensión", "Universal", 35, 10.50))
listado.agregar_repuesto(Repuesto(48, "SKF", "Rodamientos de rueda", "Universal", 60, 45.25))
listado.agregar_repuesto(Repuesto( 49, "Brembo", "Kit de freno de tambor", "Universal", 40, 90.99))
listado.agregar_repuesto(Repuesto(50, "Bosch", "Kit de reparación de frenos antibloqueo (ABS)", "Universal", 30, 120.75))
'''