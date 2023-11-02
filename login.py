import flet as ft
from flet import *

class LoginForm(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Container(
            width=400,
            height=300,
            bgcolor="#111827",  # Fondo oscuro
            border_radius=20,
            content=ft.Column(
                alignment="center",
                spacing=20,
                controls=[
                    ft.Text("Iniciar Sesión", size=24, color="white", weight="w700"),
                    ft.TextField(
                        hint_text="Nombre de Usuario",
                        border_color="transparent",
                        bgcolor="#1e293b",
                        text_color="white",
                    ),
                    ft.TextField(
                        hint_text="Contraseña",
                        border_color="transparent",
                        bgcolor="#1e293b",
                        text_color="white",
                        password=True,
                    ),
                    ft.ElevatedButton(
                        content=ft.Text("Ingresar", size=18, weight="w700"),
                        bgcolor="#f7ce7c",
                        color="black",
                        width=200,
                    ),
                ],
            ),
        )

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#111827"  # Color de fondo oscuro
    page.add(LoginForm())
    page.update()

if __name__ == "__main__":
    flet.app(target=main)
