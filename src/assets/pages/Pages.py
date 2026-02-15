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
    def __init__(self, page):
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
                    ft.TextField(label="Данные", multiline=True),
                    ft.Divider(),
                    ft.Text(
                        "Параметры шифрования", 
                        size=16
                    ),
                    ft.DropdownM2(
                        label="Метод",
                        options=[
                            ft.dropdown.Option("XOR"),
                            ft.dropdown.Option("Шифр Цезаря")
                        ],
                    ),
                    ft.Divider(),
                    ft.Text(
                        "Безопасность", 
                        size=16
                    ),
                    ft.TextField(
                        label="Ключ шифрования", password=True, can_reveal_password=True
                    ),
                    ft.TextField(
                        label="Повтор", password=True, can_reveal_password=True
                    ),
                    ft.Divider(),
                    ft.Button("Подтвердить", icon=ft.Icons.CHECK),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ADAPTIVE
            ),
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    def get_content(self):
        return self.content
    

# --- Image encryption page ---
class IEP():
    def __init__(self, page):
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(value="Шифрование изображения"),
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