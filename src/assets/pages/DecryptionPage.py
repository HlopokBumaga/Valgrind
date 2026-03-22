'''
Valgrind | DecryptionPage.py

Creating the decryption page.
'''

import flet as ft
import asyncio
from ..methods.xor import xor
from ..methods.caesar import caesar
from ..methods.vigener import vigener
from ..methods.checksum import checksum

# --- Load cryptographers ---
crypto_xor = xor()
crypto_caesar = caesar()
crypto_vigener = vigener()
crypto_checksum = checksum()


# --- Decryption page ---
class DP:
    def __init__(self, page, local):
        # --- Flet page ---
        self.page = page

        # --- Language vocabulary ---
        self.local = local

        # --- Initialization references ---
        self.data = ft.Ref[ft.TextField]()
        self.password = ft.Ref[ft.TextField]()
        self.checksum = ft.Ref[ft.TextField]()

        self.method = ft.Ref[ft.DropdownM2]()

        self.confirm = ft.Ref[ft.Button]()

        self.error = ft.Ref[ft.SnackBar]()

        self.result_text = ft.Ref[ft.TextField]()
        self.checksum_text = ft.Ref[ft.Text]()
        self.checksum_icon = ft.Ref[ft.Icon]()

        # --- Information bars ---
        self.error_bar = ft.SnackBar("Error", bgcolor=ft.Colors.ERROR, ref=self.error)

        self.result_bar = ft.AlertDialog(
            title=self.local["encryption_page"][9],
            content=ft.Column(
                [
                    ft.TextField(
                        label=self.local["encryption_page"][10], read_only=True, ref=self.result_text
                    ),
                    ft.Row(
                        [
                            ft.Icon(
                                icon=ft.Icons.CHECK,
                                ref=self.checksum_icon
                            ),
                            ft.Text(
                                "Контрольные суммы совпадают.",
                                size=15,
                                ref=self.checksum_text
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        '''
        Creating the encryption page
        '''
        self.content = ft.Row(
            ft.Column(
                [
                    ft.Column(
                        [
                            ft.Text(self.local["decryption_page"][4], size=16),
                            # --- Data text field ---
                            ft.TextField(
                                label=self.local["encryption_page"][3],
                                max_length=30,
                                on_change=self.change_confirm_button_state,
                                ref=self.data,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        [
                            ft.Text(self.local["decryption_page"][2], size=16),
                            ft.DropdownM2(
                                label=self.local["encryption_page"][5],
                                options=[
                                    ft.dropdown.Option(self.local["methods"][0]),
                                    ft.dropdown.Option(self.local["methods"][1]),
                                    ft.dropdown.Option(self.local["methods"][2]),
                                ],
                                on_change=self.change_confirm_button_state,
                                ref=self.method,
                            ),
                            ft.Divider(),
                            # --- Password text field ---
                            ft.TextField(
                                label=self.local["decryption_page"][3],
                                password=True,
                                can_reveal_password=True,
                                on_change=self.change_confirm_button_state,
                                ref=self.password,
                            ),
                            # --- Checksum text field ---
                            ft.TextField(
                                label=self.local["decryption_page"][1],
                                on_change=self.change_confirm_button_state,
                                ref=self.checksum,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Button(
                        self.local["encryption_page"][8],
                        icon=ft.Icons.CHECK,
                        on_click=self.confirm_button,
                        ref=self.confirm,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.HIDDEN,
                spacing=20,
            ),
            expand=True,
            alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )

        self.DecryptionAppBar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda: asyncio.create_task(self.page.push_route("/")),
            ),
            title=ft.Text(self.local["decryption_page"][0]),
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER,
        )
    
    def get_content(self):
        return self.content

    def confirm_button(self, e):
        self.confirm.current.disabled = True

        if self.method.current.value == self.local["methods"][0]:  # XOR
            try:
                result = crypto_xor.crypt(
                    self.data.current.value, self.password.current.value, self.local
                )
                self.result_text.current.value = result

                if crypto_checksum.check(
                    self.data.current.value.encode(), 
                    self.password.current.value.encode(),
                    self.checksum.current.value
                ):
                    self.checksum_icon.current.icon = ft.Icons.CHECK
                    self.checksum_text.current.value = self.local["decryption_page"][5]
                else:
                    self.checksum_icon.current.icon = ft.Icons.CLOSE
                    self.checksum_text.current.value = self.local["decryption_page"][6]
                
                self.page.show_dialog(self.result_bar)
            except ValueError as err:
                self.error.current.content = f"ValueError: {err}"
                self.page.show_dialog(self.error_bar)
        elif self.method.current.value == self.local["methods"][1]: # Caesar
            try:
                result = crypto_caesar.crypt(
                    self.data.current.value, self.password.current.value, "De"
                )
                self.result_text.current.value = result

                if crypto_checksum.check(
                    self.data.current.value.encode(), 
                    self.password.current.value.encode(),
                    self.checksum.current.value
                ):
                    self.checksum_icon.current.icon = ft.Icons.CHECK
                    self.checksum_text.current.value = self.local["decryption_page"][5]
                else:
                    self.checksum_icon.current.icon = ft.Icons.CLOSE
                    self.checksum_text.current.value = self.local["decryption_page"][6]

                self.page.show_dialog(self.result_bar)
            except ValueError as err:
                self.error.current.content = f"ValueError: {err}"
                self.page.show_dialog(self.error_bar)
        elif self.method.current.value == self.local["methods"][2]: # Vigener
            try:
                result = crypto_vigener.crypt(
                    self.data.current.value, self.password.current.value, "De"
                )
                self.result_text.current.value = result

                if crypto_checksum.check(
                    self.data.current.value.encode(), 
                    self.password.current.value.encode(),
                    self.checksum.current.value
                ):
                    self.checksum_icon.current.icon = ft.Icons.CHECK
                    self.checksum_text.current.value = self.local["decryption_page"][5]
                else:
                    self.checksum_icon.current.icon = ft.Icons.CLOSE
                    self.checksum_text.current.value = self.local["decryption_page"][6]
                
                self.page.show_dialog(self.result_bar)
            except ValueError as err:
                self.error.current.content = f"ValueError: {err}"
                self.page.show_dialog(self.error_bar)
        else:  # Method is not selected
            self.error.current.content = (
                "invalid method: the decryption method is not selected"
            )
            self.page.show_dialog(self.error_bar)

    def change_confirm_button_state(self):
        self.confirm.current.disabled = False