from Cliente import Cliente, ListadoClientes
from Automovil import Automovil, InventarioAutomoviles
from Repuesto import Repuesto, ListadoRepuestos
from Empleado import Empleado, ListadoEmpleados
from Ticket import Ticket

def main():
    ancho_pantalla = 150
    while True:
        print("")
        print("********* Bienvenido a la Concesionaria Arturo Jauretche *********".center(ancho_pantalla))
        print("****** Menu Principal ******".center(ancho_pantalla))
        print("")
        print("1. Clientes".center(ancho_pantalla))
        print("2. Vehiculos".center(ancho_pantalla))
        print("3. Repuestos".center(ancho_pantalla))
        print("4. Empleados".center(ancho_pantalla))
        print("5. Orden de compra".center(ancho_pantalla))
        print("6. Salir".center(ancho_pantalla))
        print("")

        opcion = input("Seleccione una opción: \n".center(ancho_pantalla) + "           ")

        if opcion == "1":
            print("")
            print("*** Clientes ***".center(ancho_pantalla))
            print("")
            print("1. Clientes registrados")
            print("2. Agregar un cliente")
            print("3. Buscar cliente")
            print("4. Menu Principal")
            print("5. Salir")
            print("")

            opcion_if_1 = input("Seleccione una opción: ")

            if opcion_if_1 == "1":
                ListadoClientes().mostrar_listado()
                print("")

            elif opcion_if_1 == "2":
                id = int(input("Ingrese el ID: "))
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                telefono = input("Ingrese el teléfono: ")
                correo = input("Ingrese el correo: ")
                nuevo_cliente = Cliente(id, nombre, apellido, telefono, correo)
                ListadoClientes().agregar_cliente(nuevo_cliente)
                ListadoClientes().mostrar_listado()
                print(nuevo_cliente)
                print("Cliente agregado exitosamente.")

            elif opcion_if_1 == "3":
                id_buscado = int(input("Ingrese el ID del cliente buscado: "))
                listado_clientes = ListadoClientes()
                cliente = listado_clientes.buscar_cliente(id_buscado)
                if cliente:
                    print("")
                    print("¡¡¡Cliente encontrado!!!")
                    print(cliente)
                else:
                    print("Cliente no registrado.")

            elif opcion_if_1 == "4":
                pass

            elif opcion_if_1 == "5":
                print("Gracias por usar nuestro sistema. ¡Hasta luego!".center(ancho_pantalla))
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")

        elif opcion == "2":
            print("")
            print("*** Vehiculos ***".center(ancho_pantalla))
            print("")
            print("1. Vehiculos registrados")
            print("2. Agregar un vehiculo")
            print("3. Buscar vehiculo")
            print("4. Menu Principal")
            print("5. Salir")
            print("")

            opcion_if_2 = input("Seleccione una opción: ")

            if opcion_if_2 == "1":
                InventarioAutomoviles().mostrar_inventario()
                print("")

            elif opcion_if_2 == "2":
                id = int(input("Ingrese el ID: "))
                marca = input("Ingrese el marca: ")
                modelo = input("Ingrese el modelo: ")
                anio = input("Ingrese el año: ")
                color = input("Ingrese el color: ")
                carroceria = input("Ingrese el tipo de carroceria: ")
                precio = input("Ingrese el precio: ")
                kilometraje = input("Ingrese el kilometraje: ")
                transmision = input("Ingrese el tipo de transmision: ")
                combustible = input("Ingrese el tipo de combustible: ")
                estado = input("Ingrese el estado: ")
                nuevo_vehiculo = Automovil(id, marca, modelo, anio, color, carroceria, precio, kilometraje, transmision, combustible, estado)
                InventarioAutomoviles().agregar_automovil(nuevo_vehiculo)
                InventarioAutomoviles().mostrar_inventario()
                print(nuevo_vehiculo)
                print("Automovil agregado exitosamente.")

            elif opcion_if_2 == "3":
                print("Opciones de busqueda")
                print("1. Por ID")
                print("2. Por marca")
                print("3. Por estado")
                print("4. Menu Principal")

                patron_busqueda = input("Seleccione una opcion: ")

                if patron_busqueda == "1":
                    id_buscado = int(input("Ingrese el ID del vehiculo buscado: "))
                    lista_autos = InventarioAutomoviles()
                    auto = lista_autos.buscar_automovil_id(id_buscado)
                    if auto:
                        print("")
                        print("¡¡¡Vehiculo encontrado!!!")
                        print(auto)
                    else:
                        print("Vehiculo inexistente con ese registro.")

                elif patron_busqueda == "2":
                    marca_buscada = input("Ingrese la marca del vehiculo buscado: ")
                    lista_autos = InventarioAutomoviles()
                    auto = lista_autos.buscar_automovil_marca(marca_buscada)
                    if auto:
                        print("")
                        print("¡¡¡Vehiculo encontrado!!!")
                        print(auto)
                    else:
                        print("Vehiculo inexistente con ese registro.")

                elif patron_busqueda == "3":
                    estado_buscado = input("Ingrese el estado de. vehiculo (Nuevo/Usado: ")
                    lista_autos = InventarioAutomoviles()
                    condicion = lista_autos.buscar_automovil_estado(estado_buscado)
                    if condicion:
                        print("")
                        print("¡¡¡Vehiculo encontrado!!!")
                        for auto in condicion:
                            print(auto)
                    else:
                        print("Vehiculo inexistente con ese registro.")

                elif opcion_if_2 == "4":
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")

            elif opcion_if_2 == "4":
                pass

            elif opcion_if_2 == "5":
                print("Gracias por usar nuestro sistema. ¡Hasta luego!".center(ancho_pantalla))
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")

        elif opcion == "3":
            print("")
            print("*** Repuestos ***".center(ancho_pantalla))
            print("")
            print("1. Inventario de repuestos")
            print("2. Agregar un repuesto")
            print("3. Buscar repuesto")
            print("4. Menu Principal")
            print("5. Salir")
            print("")

            opcion_if_3 = input("Seleccione una opción: ")

            if opcion_if_3 == "1":
                ListadoRepuestos().mostrar_listado()
                print("")

            elif opcion_if_3 == "2":
                id = int(input("Ingrese el ID: "))
                marca = input("Ingrese el marca: ")
                nombre = input("Ingrese el nombre: ")
                vehiculo = input("Ingrese el vehiculo: ")
                cantidad = input("Ingrese la cantidad: ")
                precio = input("Ingrese el precio: ")

                nuevo_repuesto = Repuesto(id, marca, nombre, vehiculo, cantidad, precio)
                ListadoRepuestos().agregar_repuesto(nuevo_repuesto)
                ListadoRepuestos().mostrar_listado()
                print(nuevo_repuesto)
                print("Repuesto agregado exitosamente al inventario.")

            elif opcion_if_3 == "3":
                print("Opciones de busqueda")
                print("1. Por ID")
                print("2. Por nombre")
                print("3. Menu Principal")

                patron_busqueda_repuesto = input("Seleccione una opcion: ")

                if patron_busqueda_repuesto == "1":
                    id_buscado = int(input("Ingrese el ID del repuesto buscado: "))
                    lista_repuestos = ListadoRepuestos()
                    repuesto = lista_repuestos.buscar_repuesto_id(id_buscado)
                    if repuesto:
                        print("")
                        print("¡¡¡Repuesto encontrado!!!")
                        print(repuesto)
                    else:
                        print("Repuesto inexistente en el inventario con ese registro.")

                elif patron_busqueda_repuesto == "2":
                    nombre_buscado = input("Ingrese el nombre del repuesto buscado: ")
                    lista_repuestos = ListadoRepuestos()
                    repuesto = lista_repuestos.buscar_repuesto_nombre(nombre_buscado)
                    if repuesto:
                        print("")
                        print("¡¡¡Repuesto encontrado!!!")
                        for item in repuesto:
                            print(item)
                    else:
                        print("Repuesto inexistente con ese registro.")

                elif patron_busqueda_repuesto == "3":
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")

        elif opcion == "4":
            print("")
            print("*** Empleados ***".center(ancho_pantalla))
            print("")
            print("1. Empleados registrados")
            print("2. Agregar un empleado")
            print("3. Buscar empleado")
            print("4. Menu Principal")
            print("5. Salir")
            print("")

            opcion_if_4 = input("Seleccione una opcion: ")

            if opcion_if_4 == "1":
                ListadoEmpleados().mostrar_listado()
                print("")

            elif opcion_if_4 == "2":
                id = int(input("Ingrese el ID: "))
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                cargo = input("Ingrese el cargo: ")
                correo = input("Ingrese el correo: ")
                telefono = input("Ingrese el teléfono: ")
                direccion = input("Ingrese la direccion: ")
                salario = input("Ingrese el salario: ")
                nuevo_empleado = Empleado(id, nombre, apellido, cargo, correo, telefono, direccion, salario)
                ListadoEmpleados().agregar_empleado(nuevo_empleado)
                ListadoEmpleados().mostrar_listado()
                print(nuevo_empleado)
                print("Empleado registrado exitosamente.")

            elif opcion_if_4 == "3":
                id_buscado = int(input("Ingrese el ID del empleado buscado: "))
                listado_empleados = ListadoEmpleados()
                empleado = (listado_empleados.buscar_empleado(id_buscado))
                if empleado:
                    print("")
                    print("¡¡¡Empleado encontrado!!!")
                    print(empleado)
                else:
                    print("Empleado inexistente.")

            elif opcion_if_4 == "4":
                pass

            elif opcion_if_4 == "5":
                print("Gracias por usar nuestro sistema. ¡Hasta luego!".center(ancho_pantalla))
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")

        elif opcion == "5":
            print("")
            print("********* Orden de compra *********".center(ancho_pantalla))
            print("")
            # Solicitar al usuario que seleccione un cliente, empleado, auto y repuesto
            id_cliente = int(input("Ingrese el ID del cliente: "))
            id_empleado = int(input("Ingrese el ID del empleado: "))
            id_auto = int(input("Ingrese el ID del auto: "))
            id_repuesto = int(input("Ingrese el ID del repuesto: "))

#Invocar los metodos para la busqueda
            listado_clientes = ListadoClientes()
            clientes = listado_clientes.obtener_listado()
            listado_empleados = ListadoEmpleados()
            empleados = listado_empleados.obtener_listado()
            inventario_autos = InventarioAutomoviles()
            autos = inventario_autos.obtener_listado()
            lista_repuestos = ListadoRepuestos()
            repuestos = lista_repuestos.obtener_listado()

# Buscar las instancias correspondientes en las listas
            cliente = next((c for c in clientes if c.id == id_cliente), None)
            empleado = next((e for e in empleados if e.id == id_empleado), None)
            auto = next((a for a in autos if a.id == id_auto), None)
            repuesto = next((r for r in repuestos if r.id == id_repuesto), None)

# Verificar si se encontraron todas las instancias
            if not all((cliente, empleado, auto, repuesto)):
                print("Alguna de las entidades no se encontró.")

# Solicitar otros datos necesarios para el ticket
            id_ticket = input("Ingrese el ID del ticket: ")
            fecha_hora_compra = input("Ingrese la fecha y hora de la compra (YYYY-MM-DD HH:MM): ")
            total_compra = float(input("Ingrese el monto total de la compra: "))
            detalle_articulo = input("Ingrese el detalle del artículo: ")
            metodo_pago = input("Ingrese el método de pago: ")

# Crear una nueva instancia de Ticket con los datos proporcionados
            ticket = Ticket(id_ticket, cliente, empleado, auto, repuesto, fecha_hora_compra, total_compra, detalle_articulo, metodo_pago)

# Imprimir el ticket creado
            print("")
            print("Ticket creado con éxito")
            print("")
            print(ticket)

            factura = input("¿Desea descargar el comprobante en PDF? (Y/N): ")
            if factura.lower() == "y":
                ticket.generar_pdf("ticket.pdf")
                print("Comprobante descargado como 'ticket.pdf'.")
            else:
                print("Comprobante no descargado.")

        elif opcion == "6":
            print("Gracias por usar nuestro sistema. ¡Hasta luego!".center(ancho_pantalla))
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    main()
