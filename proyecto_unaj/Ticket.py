from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Ticket:
    def __init__(self, id_ticket, id_cliente, id_empleado, id_auto, id_repu, fecha_hora_compra, total_compra, detalle_articulo, metodo_pago):
        self.id_ticket = id_ticket
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.id_auto = id_auto
        self.id_repu = id_repu
        self.fecha_hora_compra = fecha_hora_compra
        self.total_compra = total_compra
        self.detalle_articulo = detalle_articulo
        self.metodo_pago = metodo_pago

    def __str__(self):
        ticket_dict = {
            "ID Ticket": self.id_ticket,
            "ID Cliente": self.id_cliente,
            "ID Empleado": self.id_empleado,
            "ID Auto": self.id_auto,
            "ID Repuesto": self.id_repu,
            "Fecha/Hora Compra": self.fecha_hora_compra,
            "Total": self.total_compra,
            "Detalle": self.detalle_articulo,
            "Metodo de Pago": self.metodo_pago
        }

        formatted_ticket = ""
        for key, value in ticket_dict.items():
            formatted_ticket += f"{key}: {value}\n"

        return formatted_ticket.strip()

    def generar_pdf(self, filename):
        ticket_info = [
            ("ID Ticket", str(self.id_ticket)),
            ("ID Cliente", str(self.id_cliente)),
            ("ID Empleado", str(self.id_empleado)),
            ("ID Auto", str(self.id_auto)),
            ("ID Repuesto", str(self.id_repu)),
            ("Fecha/Hora Compra", str(self.fecha_hora_compra)),
            ("Total", str(self.total_compra)),
            ("Detalle", self.detalle_articulo),
            ("Metodo de Pago", self.metodo_pago)
        ]

        c = canvas.Canvas(filename, pagesize=letter)
        y = 750
        for key, value in ticket_info:
            c.drawString(50, y, f"{key}: {value}")
            y -= 20
        c.save()

