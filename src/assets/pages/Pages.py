import flet as ft


# --- Main page ---
class MP():
    def __init__(self, page, light_icon_path, dark_icon_path):
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Image(
                            src=light_icon_path if page.theme_mode.value == "dark" else dark_icon_path,
                            width=300
                        ),
                        ft.Text(
                            value="Программа для шифрования данных.",
                            size=17,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Text(
                            value="Выберите цель шифрования в меню снизу.",
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
        return self.content


# --- Text encryption page ---
class TEP():
    def __init__(self, page, local):
        # --- Load language vocabulary ---
        self.local = local

        # --- Data containers ---
        self.data = ft.Ref[ft.TextField]()
        self.password = ft.Ref[ft.TextField]()
        self.password_repeat = ft.Ref[ft.TextField]()

        self.method = ft.Ref[ft.DropdownM2]()
        self.description = ft.Ref[ft.Text]()

        # --- Text page form ---
        self.content = ft.Row(
            ft.Column(
                [
                    ft.Text(
                        "Шифрование текста", 
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
                                label=ft.Text("Зашифровать"),
                            ),
                            ft.Segment(
                                value="De",
                                label=ft.Text("Расшифровать"),
                            ),
                        ],
                    ),

                    # --- Data text field ---
                    ft.TextField(
                        label="Данные", 
                        multiline=True,
                        ref=self.data
                    ),
                    
                    ft.Divider(),
                    ft.Text(
                        "Параметры шифрования", 
                        size=16
                    ),
                    ft.DropdownM2(
                        label="Метод",
                        options=[
                            ft.dropdown.Option(self.local["methods"][0]),
                            ft.dropdown.Option(self.local["methods"][1]),
                            ft.dropdown.Option(self.local["methods"][2])
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
                        label="Ключ шифрования", 
                        password=True, 
                        can_reveal_password=True,
                        ref=self.password
                    ),

                    # --- Repeat password text field ---
                    ft.TextField(
                        label="Повтор", 
                        password=True,
                        can_reveal_password=True,
                        ref=self.password_repeat
                    ),

                    ft.Divider(),
                    ft.Button(
                        "Подтвердить", 
                        icon=ft.Icons.CHECK, 
                        on_click=self.confirm_button
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ADAPTIVE,
            ),
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    def get_content(self):
        return self.content

    # --- Confirm function ---
    def confirm_button(self, e):
        print(self.data.current.value)

    # --- Change method and get description ---
    def change_method(self, e):
        self.description.current.value = self.local["description_methods"][self.local["methods"].index(self.method.current.value)]


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