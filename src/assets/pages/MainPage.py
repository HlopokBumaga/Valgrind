'''
Valgrind | MainPage.py

Creating the main page.
'''

import flet as ft

# --- Paths ---
MAIN_ICON_PATH_DARK = "src/assets/logos/Logo_Black_Only_Text.svg"
MAIN_ICON_PATH_LIGHT = "src/assets/logos/Logo_White_Only_Text.svg"


# --- Main page ---
class MP:
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
        self.main_logo = ft.Ref[ft.Image]()

        '''
        Creating the main page

        Logo with a change
        depending on the theme, description.
        '''
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Image(
                            src=self.set_logo_by_theme(), width=300, ref=self.main_logo
                        ),
                        ft.Text(
                            value=self.local["main_page"][0],
                            size=17,
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Text(value=self.local["main_page"][1], italic=True),
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
        self.main_logo.current.src = self.set_logo_by_theme()

        return self.content

    def set_logo_by_theme(self):
        if self.page.theme_mode.value == "dark":
            return MAIN_ICON_PATH_LIGHT
        else:
            return MAIN_ICON_PATH_DARK