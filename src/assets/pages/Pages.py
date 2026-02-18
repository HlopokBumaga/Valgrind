import flet as ft
import json
from ..methods.xor import xor

# --- Load cryptographers ---
crypto_xor = xor()


# --- Main page ---
class MP():
    def __init__(self, page, light_icon_path, dark_icon_path, local):
        self.page = page

        # --- Load language vocabulary ---
        self.local = local

        # --- Data containers ---
        self.logo = ft.Ref[ft.Image]()
        self.light = light_icon_path
        self.dark = dark_icon_path

        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Image(
                            src = self.light if self.page.theme_mode.value == "dark" else self.dark,
                            width=300,
                            ref=self.logo
                        ),
                        ft.Text(
                            value=self.local["main_page"][0],
                            size=17,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Text(
                            value=self.local["main_page"][1],
                            italic=True
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    def get_content(self):
        self.logo.current.src = self.light if self.page.theme_mode.value == "dark" else self.dark

        return self.content


# --- Text encryption page ---
class TEP():
    def __init__(self, page, local):
        self.page = page

        # --- Load language vocabulary ---
        self.local = local

        # --- Data containers ---
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
        self.error_bar = ft.SnackBar(
            "Error",
            bgcolor=ft.Colors.ERROR,
            ref=self.error
        )

        self.result_bar = ft.AlertDialog(
            title=self.local["text_page"][9],
            content=ft.TextField(
                label=self.local["text_page"][10],
                read_only=True,
                ref=self.result_text
            )
        )

        # --- Text page form ---
        self.content = ft.Row(
            ft.Column(
                [
                    ft.Column(
                        [
                            ft.Text(
                                self.local["text_page"][0], 
                                weight=ft.FontWeight.W_600,
                                size=17
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
                            ),

                            # --- Data text field ---
                            ft.TextField(
                                label=self.local["text_page"][3], 
                                multiline=True,
                                on_change=self.change_confirm_button_state,
                                ref=self.data
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                self.local["text_page"][4], 
                                size=16
                            ),
                            ft.DropdownM2(
                                label=self.local["text_page"][5],
                                options=[
                                    ft.dropdown.Option(self.local["methods"][0]),
                                    ft.dropdown.Option(self.local["methods"][1], disabled=True),
                                    ft.dropdown.Option(self.local["methods"][2], disabled=True)
                                ],
                                on_change=self.change_method,
                                ref=self.method
                            ),

                            # --- Method description ---
                            ft.Text(
                                "",
                                size=14,
                                width=300,
                                text_align=ft.TextAlign.JUSTIFY,
                                ref=self.description
                            ),
                            
                            ft.Divider(),

                            # --- Password text field ---
                            ft.TextField(
                                label=self.local["text_page"][6], 
                                password=True, 
                                can_reveal_password=True,
                                on_change=self.change_confirm_button_state,
                                ref=self.password
                            ),

                            # --- Repeat password text field ---
                            ft.TextField(
                                label=self.local["text_page"][7], 
                                password=True,
                                can_reveal_password=True,
                                on_change=self.change_confirm_button_state,
                                ref=self.password_repeat
                            ),

                            # --- Keys description ---
                            ft.Text(
                                "",
                                size=14,
                                width=300,
                                text_align=ft.TextAlign.JUSTIFY,
                                ref=self.description_key
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Button(
                        self.local["text_page"][8], 
                        icon=ft.Icons.CHECK, 
                        on_click=self.confirm_button,
                        ref=self.confirm
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.HIDDEN,
                spacing=20
            ),
            expand=True,
            alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
    
    def get_content(self):
        return self.content

    # --- Confirm function ---
    def confirm_button(self, e):
        self.confirm.current.disabled = True

        if self.method.current.value == self.local["methods"][0]: # XOR
            if self.password.current.value == self.password_repeat.current.value:
                try:
                    self.result_text.current.value = crypto_xor.crypt(self.data.current.value, self.password.current.value)
                    self.page.show_dialog(self.result_bar)
                except ValueError as err:
                    self.error.current.content = f"ValueError: {err}"
                    self.page.show_dialog(self.error_bar)
            else:
                self.error.current.content = "Confirmation error: keys do not match"
                self.page.show_dialog(self.error_bar)

        else: # Method is not selected
            self.error.current.content = "invalid method: the encryption method is not selected"
            self.page.show_dialog(self.error_bar)

    
    def change_confirm_button_state(self):
        self.confirm.current.disabled = False

    # --- Change method and get description ---
    def change_method(self, e):
        self.confirm.current.disabled = False
        self.description.current.value = self.local["description_methods"][self.local["methods"].index(self.method.current.value)]
        self.description_key.current.value = self.local["description_methods_keys"][self.local["methods"].index(self.method.current.value)]


# --- Image encryption page ---
class IEP():
    def __init__(self, page):
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


# --- Settings page ---
class SP():
    def __init__(self, page, nav_bar, back_button, settings_path, small_logo, dark_icon_path, light_icon_path):
        # --- Data containers ---
        self.theme_button = ft.Ref[ft.SegmentedButton]()
        self.language_button = ft.Ref[ft.SegmentedButton]()
        self.small_logo = small_logo
        self.light = light_icon_path
        self.dark = dark_icon_path

        # --- Load main elements ---
        self.page = page
        self.back_button = back_button
        self.nav_bar = nav_bar
        self.settings_path = settings_path

        # --- Load settings ---
        with open(self.settings_path, "r") as file:
            config = json.load(file)

        # --- Settings page form ---
        self.content = ft.Row(
            ft.Column(
                [
                    ft.Text(
                        "Настройки", 
                        weight=ft.FontWeight.W_600,
                        size=17
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "Тема интерфейса", 
                                size=16
                            ),
                            ft.SegmentedButton(
                                selected_icon=ft.Icon(ft.Icons.CHECK),
                                selected=[config["theme"]],
                                allow_empty_selection=False,
                                segments=[
                                    ft.Segment(
                                        value="DARK",
                                        label=ft.Text("Тёмная"),
                                        icon=ft.Icons.DARK_MODE
                                    ),
                                    ft.Segment(
                                        value="LIGHT",
                                        label=ft.Text("Светлая"),
                                        icon=ft.Icons.LIGHT_MODE
                                    ),
                                ],
                                on_change=self.change_theme,
                                ref=self.theme_button
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "Язык интерфейса", 
                                size=16
                            ),
                            ft.SegmentedButton(
                                selected_icon=ft.Icon(ft.Icons.CHECK),
                                selected=[config["language"]],
                                allow_empty_selection=False,
                                segments=[
                                    ft.Segment(
                                        value="RU",
                                        label=ft.Text("Русский"),
                                    ),
                                    ft.Segment(
                                        value="EN",
                                        label=ft.Text("English"),
                                    ),
                                ],
                                ref=self.language_button
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.HIDDEN,
                spacing=20
            ),
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def get_content(self):
        self.back_button.current.visible = True
        self.nav_bar.visible = False

        return self.content
    
    # --- Change theme ---
    def change_theme(self):
        with open(self.settings_path, "r") as file:
            config = json.load(file)
            config["theme"] = self.theme_button.current.selected[0]

        with open(self.settings_path, "w") as file:
            json.dump(config, file, indent=4)
        
        if self.theme_button.current.selected[0] == "DARK":
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT

        self.small_logo.current.src = self.light if self.page.theme_mode.value == "dark" else self.dark