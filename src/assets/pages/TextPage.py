'''
Valgrind | TextPage.py

Creating the text page.
'''

import flet as ft
from ..methods.xor import xor
from ..methods.caesar import caesar

# --- Load cryptographers ---
crypto_xor = xor()
crypto_caesar = caesar()


# --- Text encryption page ---
class TEP:
    '''
    Init class

    Parameters:
    page - flet page,
    local - localization vocabulary.
    '''
    def __init__(self, page, local):
        # --- Flet page ---
        self.page = page

        # --- Language vocabulary ---
        self.local = local

        # --- Initialization references ---
        self.target = ft.Ref[ft.SegmentedButton]()

        self.data = ft.Ref[ft.TextField]()
        self.password = ft.Ref[ft.TextField]()
        self.password_repeat = ft.Ref[ft.TextField]()

        self.method = ft.Ref[ft.DropdownM2]()
        self.description = ft.Ref[ft.Text]()
        self.description_key = ft.Ref[ft.Text]()

        self.confirm = ft.Ref[ft.Button]()

        self.error = ft.Ref[ft.SnackBar]()

        self.result_text = ft.Ref[ft.TextField]()

        # --- Information bars ---
        self.error_bar = ft.SnackBar("Error", bgcolor=ft.Colors.ERROR, ref=self.error)

        self.result_bar = ft.AlertDialog(
            title=self.local["text_page"][9],
            content=ft.TextField(
                label=self.local["text_page"][10], read_only=True, ref=self.result_text
            ),
        )

        '''
        Creating the text encryption page
        '''
        self.content = ft.Row(
            ft.Column(
                [
                    ft.Column(
                        [
                            ft.Text(
                                self.local["text_page"][0],
                                weight=ft.FontWeight.W_600,
                                size=17,
                            ),
                            ft.SegmentedButton(
                                selected_icon=ft.Icon(ft.Icons.CHECK),
                                selected=["En"],
                                allow_empty_selection=False,
                                segments=[
                                    ft.Segment(
                                        value="En",
                                        label=ft.Text(self.local["text_page"][1]),
                                    ),
                                    ft.Segment(
                                        value="De",
                                        label=ft.Text(self.local["text_page"][2]),
                                    ),
                                ],
                                ref=self.target
                            ),
                            # --- Data text field ---
                            ft.TextField(
                                label=self.local["text_page"][3],
                                multiline=True,
                                on_change=self.change_confirm_button_state,
                                ref=self.data,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        [
                            ft.Text(self.local["text_page"][4], size=16),
                            ft.DropdownM2(
                                label=self.local["text_page"][5],
                                options=[
                                    ft.dropdown.Option(self.local["methods"][0]),
                                    ft.dropdown.Option(self.local["methods"][1]),
                                    ft.dropdown.Option(
                                        self.local["methods"][2], disabled=True
                                    ),
                                ],
                                on_change=self.change_method,
                                ref=self.method,
                            ),
                            # --- Method description ---
                            ft.Text(
                                "",
                                size=14,
                                width=300,
                                text_align=ft.TextAlign.JUSTIFY,
                                ref=self.description,
                            ),
                            ft.Divider(),
                            # --- Password text field ---
                            ft.TextField(
                                label=self.local["text_page"][6],
                                password=True,
                                can_reveal_password=True,
                                on_change=self.change_confirm_button_state,
                                ref=self.password,
                            ),
                            # --- Repeat password text field ---
                            ft.TextField(
                                label=self.local["text_page"][7],
                                password=True,
                                can_reveal_password=True,
                                on_change=self.change_confirm_button_state,
                                ref=self.password_repeat,
                            ),
                            # --- Keys description ---
                            ft.Text(
                                "",
                                size=14,
                                width=300,
                                text_align=ft.TextAlign.JUSTIFY,
                                ref=self.description_key,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Button(
                        self.local["text_page"][8],
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

    def get_content(self):
        return self.content

    '''
    Confirm function

    1) Lock the button to avoid double-clicking. 
    2) Check the selected method, otherwise we raise an exception. 
    3) Check if the keys match, otherwise we raise an exception. 
    4) Encrypt it and output the result.
    '''
    def confirm_button(self, e):
        self.confirm.current.disabled = True

        if self.method.current.value == self.local["methods"][0]:  # XOR
            if self.password.current.value == self.password_repeat.current.value:
                try:
                    self.result_text.current.value = crypto_xor.crypt(
                        self.data.current.value, self.password.current.value
                    )
                    self.page.show_dialog(self.result_bar)
                except ValueError as err:
                    self.error.current.content = f"ValueError: {err}"
                    self.page.show_dialog(self.error_bar)
            else:
                self.error.current.content = "Confirmation error: keys do not match"
                self.page.show_dialog(self.error_bar)
        elif self.method.current.value == self.local["methods"][1]: # Caesar
            if self.password.current.value == self.password_repeat.current.value:
                try:
                    self.result_text.current.value = crypto_caesar.crypt(
                        self.data.current.value, self.password.current.value, self.target.current.selected[0]
                    )
                    self.page.show_dialog(self.result_bar)
                except ValueError as err:
                    self.error.current.content = f"ValueError: {err}"
                    self.page.show_dialog(self.error_bar)
            else:
                self.error.current.content = "Confirmation error: keys do not match"
                self.page.show_dialog(self.error_bar)
        else:  # Method is not selected
            self.error.current.content = (
                "invalid method: the encryption method is not selected"
            )
            self.page.show_dialog(self.error_bar)

    def change_confirm_button_state(self):
        self.confirm.current.disabled = False

    '''
    Change method and get description

    Unlocking the button.
    We take the index of the method and find the description of the method 
    and the key for this index.
    '''
    def change_method(self, e):
        self.confirm.current.disabled = False
        self.description.current.value = self.local["description_methods"][
            self.local["methods"].index(self.method.current.value)
        ]
        self.description_key.current.value = self.local["description_methods_keys"][
            self.local["methods"].index(self.method.current.value)
        ]