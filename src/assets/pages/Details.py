'''
Valgrind | DetailsPage.py

Creating the details page.
'''

import flet as ft
import asyncio
from ..methods.xor import xor

# --- Load cryptographers ---
crypto_xor = xor()


# --- Details page ---
class DE:
    def __init__(self, page, local):
        # --- Flet page ---
        self.page = page

        # --- Language vocabulary ---
        self.local = local

        self.table = ft.Ref[ft.DataTable]()
        
        self.DetailsAppBar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda: asyncio.create_task(self.page.push_route("/")),
            ),
            title=self.local["encryption_page"][12],
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER,
        )
    
    def get_content(self, method, data, key):
        if method == self.local["methods"][0]:
            self.detail_data = crypto_xor.crypt(data, key, self.local, True)

        self.content = ft.Row(
            ft.Column(
                [
                    ft.DataTable(
                        columns=[],
                        rows=[],
                        ref=self.table
                    )
                ],
                scroll=ft.ScrollMode.HIDDEN,
                spacing=20
            ),
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO
        )

        self.table.current.columns = [ft.DataColumn(label=i) for i in self.detail_data[0]]

        for i in self.detail_data[1:]:
            self.table.current.rows.append(
                ft.DataRow(
                    cells=[ft.DataCell(cell) for cell in i]
                )
            )

        return self.content