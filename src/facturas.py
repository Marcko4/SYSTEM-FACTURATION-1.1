from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import os

class Factura:
    def __init__(self, cliente, productos, factura_num, fecha_emision):
        self.cliente = cliente
        self.productos = productos
        self.factura_num = factura_num
        self.fecha_emision = fecha_emision
        self.subtotal = sum(p.precio_unitario for p in productos)
        self.impuesto = self.subtotal * 0.15
        self.total = self.subtotal + self.impuesto

    def generar_pdf(self, pdf_path):
        # Asegúrate de que la carpeta para el PDF exista
        pdf_dir = os.path.dirname(pdf_path)
        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)

        c = canvas.Canvas(pdf_path, pagesize=letter)

        # Encabezado de la factura
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1 * inch, 10.5 * inch, "MT Security Apps")
        c.setFont("Helvetica", 10)
        c.drawString(1 * inch, 10 * inch, f"Factura No: {self.factura_num}")
        c.drawString(1 * inch, 9.5 * inch, f"Fecha de Emisión: {self.fecha_emision}")

        # Datos del cliente
        c.drawString(1 * inch, 9 * inch, f"Cliente: {self.cliente.nombre}")

        # Tabla productos 
        data = [
            ["Descripción", "Cantidad", "Precio Unitario", "Subtotal"],  # Define las columnas
            *[[p["descripcion"], p["cantidad"], p["precio_unitario"], p["precio_unitario"] * p["cantidad"]] for p in self.productos]  # Itera sobre la lista de productos
        ]

        t = Table(data)
        t.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ]))

        t.wrapOn(c, 6 * inch, 8 * inch)
        t.drawOn(c, 1 * inch, 6 * inch)

        # Total e impuestos
        c.drawString(1 * inch, 5 * inch, f"Subtotal: {self.subtotal:.2f}")
        c.drawString(1 * inch, 4.5 * inch, f"Impuesto (15%): {self.impuesto:.2f}")
        c.drawString(1 * inch, 4 * inch, f"Total: {self.total:.2f}")

        c.showPage()
        c.save()
