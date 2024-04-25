import flet as ft

from facturas import Factura
from clientes import Cliente
from productos import Producto
from usuarios import Usuario

# Lógica para el dashboard...


# Validar inicio de sesión
def validar_inicio_sesion(usuario, contrasena):
    return usuario == "admin" and contrasena == "1234"

# Pantalla de inicio de sesión
def pantalla_inicio_sesion(page):
    def iniciar_sesion(e):
        usuario = txt_usuario.value
        contrasena = txt_contrasena.value

        if validar_inicio_sesion(usuario, contrasena):
            page.clean()  # Limpiar la interfaz
            pantalla_sistema_facturacion(page)
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Usuario o contraseña incorrectos."),
                on_dismiss=lambda e: None,
            )
            page.dialog = dlg
            dlg.open = True

    txt_usuario = ft.TextField(label="Usuario")
    txt_contrasena = ft.TextField(label="Contraseña", password=True)

    btn_iniciar = ft.ElevatedButton(text="Iniciar Sesión", on_click=iniciar_sesion)

    page.add(txt_usuario, txt_contrasena, btn_iniciar)

# Pantalla principal del sistema de facturación
def pantalla_sistema_facturacion(page):
    btn_factura = ft.ElevatedButton(
        text="Crear Factura", on_click=lambda e: pantalla_crear_factura(page)
    )
    btn_clientes = ft.ElevatedButton(
        text="Lista de Clientes", on_click=lambda e: pantalla_clientes(page)
    )
    btn_productos = ft.ElevatedButton(
        text="Lista de Productos", on_click=lambda e: pantalla_productos(page)
    )

    page.add(btn_factura, btn_clientes, btn_productos)

# Pantalla para crear facturas
def pantalla_crear_factura(page):
    # Aquí va la lógica para crear una factura
    pass

# Pantalla para lista de clientes
def pantalla_clientes(page):
    # Lógica para listar clientes
    pass

# Pantalla para lista de productos
def pantalla_productos(page):
    # Lógica para listar productos
    pass

# Función principal para iniciar la aplicación Flet
def main(page: ft.Page):
    pantalla_inicio_sesion(page)

ft.app(target=main)
