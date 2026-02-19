'''
Valgrind | ImagePage.py

Creating the image encryption page.
'''

import flet as ft


# --- Image encryption page ---
class IEP():
    def __init__(self):
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(value="В разработке / In development"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    def get_content(self):
        return self.content