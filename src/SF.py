import flet as ft

def main(page):
    # Crear un objeto de texto con el mensaje
    message = ft.Text("Tobias se la come")

    # Agregar el mensaje a la página
    page.add(message)

# Ejecutar la aplicación Flet
ft.app(target=main)
