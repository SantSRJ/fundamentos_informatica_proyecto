class Automovil:
    def __init__(self, id, marca, modelo, anio, color, tipo_carroceria, precio, kilometraje, transmision, combustible, estado):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.tipo_carroceria = tipo_carroceria
        self.precio = precio
        self.kilometraje = kilometraje
        self.transmision = transmision
        self.combustible = combustible
        self.estado = estado

    def __str__(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Color: {self.color}, Tipo de Carrocería: {self.tipo_carroceria}, Precio: {self.precio}, Kilometraje: {self.kilometraje}, Transmisión: {self.transmision}, Combustible: {self.combustible}, Estado: {self.estado}"

class InventarioAutomoviles:
    def __init__(self):
        self.inventario = [
            Automovil(1, "Toyota", "Corolla", 2020, "Blanco", "Sedán", 25000, 15000, "Automática", "Gasolina",
                       "Usado"),
            Automovil(2, "Honda", "Civic", 2018, "Gris", "Sedán", 20000, 20000, "Automática", "Gasolina", "Usado"),
            Automovil(3, "Ford", "F-150", 2019, "Negro", "Camioneta", 35000, 18000, "Automática", "Gasolina",
                          "Usado"),
            Automovil(4, "Chevrolet", "Camaro", 2021, "Rojo", "Coupé", 40000, 10000, "Manual", "Gasolina", "Nuevo"),
            Automovil(5, "BMW", "Serie 3", 2020, "Azul", "Sedán", 45000, 12000, "Automática", "Gasolina", "Usado"),
            Automovil(6, "Volkswagen", "Golf", 2017, "Plateado", "Hatchback", 18000, 30000, "Automática",
                          "Gasolina", "Usado"),
            Automovil(7, "Audi", "A4", 2019, "Negro", "Sedán", 32000, 22000, "Automática", "Gasolina", "Usado"),
            Automovil(8, "Mercedes-Benz", "Clase C", 2018, "Gris", "Sedán", 35000, 25000, "Automática", "Gasolina",
                          "Usado"),
            Automovil(9, "Hyundai", "Tucson", 2020, "Blanco", "SUV", 27000, 18000, "Automática", "Gasolina",
                          "Usado"),
            Automovil(10, "Kia", "Optima", 2019, "Rojo", "Sedán", 23000, 20000, "Automática", "Gasolina", "Usado"),
            Automovil(11, "Subaru", "Outback", 2018, "Azul", "Station Wagon", 25000, 30000, "Automática",
                          "Gasolina", "Usado"),
            Automovil(12, "Volvo", "XC60", 2020, "Negro", "SUV", 40000, 15000, "Automática", "Gasolina", "Usado"),
            Automovil(13, "Mazda", "CX-5", 2019, "Gris", "SUV", 28000, 20000, "Automática", "Gasolina", "Usado"),
            Automovil(14, "Jeep", "Wrangler", 2017, "Verde", "SUV", 30000, 25000, "Manual", "Gasolina", "Usado"),
            Automovil(15, "Nissan", "Altima", 2021, "Blanco", "Sedán", 28000, 10000, "Automática", "Gasolina",
                          "Nuevo"),
            Automovil(16, "Land Rover", "Range Rover Evoque", 2019, "Plateado", "SUV", 45000, 20000, "Automática",
                          "Gasolina", "Usado"),
            Automovil(17, "Porsche", "911", 2022, "Rojo", "Coupé", 120000, 5000, "Automática", "Gasolina", "Nuevo"),
            Automovil(18, "Ferrari", "488 GTB", 2021, "Amarillo", "Coupé", 300000, 1000, "Automática", "Gasolina",
                          "Nuevo"),
            Automovil(19, "Lamborghini", "Aventador", 2020, "Naranja", "Coupé", 400000, 2000, "Automática",
                          "Gasolina", "Nuevo"),
            Automovil(20, "Bugatti", "Chiron", 2023, "Negro", "Coupé", 3000000, 100, "Automática", "Gasolina",
                          "Nuevo")
        ]

    def agregar_automovil(self, automovil):
        self.inventario.append(automovil)

    def buscar_automovil_id(self, id):
        for auto in self.inventario:
            if auto.id == id:
                return auto
        return None

    def buscar_automovil_marca(self, marca):
        for auto in self.inventario:
            if auto.marca.lower() == marca.lower():
                return auto
        return None

    def buscar_automovil_estado(self, estado):
        auto_condicion = []
        for auto in self.inventario:
            if auto.estado.lower() == estado.lower():
                auto_condicion.append(auto)

        return auto_condicion

    def mostrar_inventario(self):
        print("Inventario de Automóviles:".center(150))
        print("")
        for auto in self.inventario:
            print(auto)

    def obtener_listado(self):
        return self.inventario

'''
# Agregar algunos automóviles al inventario
inventario.agregar_automovil(Automovil(1, "Toyota", "Corolla", 2020, "Blanco", "Sedán", 25000, 15000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(2, "Honda", "Civic", 2018, "Gris", "Sedán", 20000, 20000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(3, "Ford", "F-150", 2019, "Negro", "Camioneta", 35000, 18000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(4, "Chevrolet", "Camaro", 2021, "Rojo", "Coupé", 40000, 10000, "Manual", "Gasolina", "Nuevo"))
inventario.agregar_automovil(Automovil(5, "BMW", "Serie 3", 2020, "Azul", "Sedán", 45000, 12000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(6, "Volkswagen", "Golf", 2017, "Plateado", "Hatchback", 18000, 30000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(7, "Audi", "A4", 2019, "Negro", "Sedán", 32000, 22000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(8, "Mercedes-Benz", "Clase C", 2018, "Gris", "Sedán", 35000, 25000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(9, "Hyundai", "Tucson", 2020, "Blanco", "SUV", 27000, 18000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(10, "Kia", "Optima", 2019, "Rojo", "Sedán", 23000, 20000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(11, "Subaru", "Outback", 2018, "Azul", "Station Wagon", 25000, 30000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(12, "Volvo", "XC60", 2020, "Negro", "SUV", 40000, 15000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(13, "Mazda", "CX-5", 2019, "Gris", "SUV", 28000, 20000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(14, "Jeep", "Wrangler", 2017, "Verde", "SUV", 30000, 25000, "Manual", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(15, "Nissan", "Altima", 2021, "Blanco", "Sedán", 28000, 10000, "Automática", "Gasolina", "Nuevo"))
inventario.agregar_automovil(Automovil(16, "Land Rover", "Range Rover Evoque", 2019, "Plateado", "SUV", 45000, 20000, "Automática", "Gasolina", "Usado"))
inventario.agregar_automovil(Automovil(17, "Porsche", "911", 2022, "Rojo", "Coupé", 120000, 5000, "Automática", "Gasolina", "Nuevo"))
inventario.agregar_automovil(Automovil(18, "Ferrari", "488 GTB", 2021, "Amarillo", "Coupé", 300000, 1000, "Automática", "Gasolina", "Nuevo"))
inventario.agregar_automovil(Automovil(19, "Lamborghini", "Aventador", 2020, "Naranja", "Coupé", 400000, 2000, "Automática", "Gasolina", "Nuevo"))
inventario.agregar_automovil(Automovil(20, "Bugatti", "Chiron", 2023, "Negro", "Coupé", 3000000, 100, "Automática", "Gasolina", "Nuevo"))
'''