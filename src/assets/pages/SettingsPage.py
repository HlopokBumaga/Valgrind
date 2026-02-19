'''
Valgrind | SettingsPage.py

Creating the settings page.
'''

import flet as ft
import json

# --- Paths ---
BAR_ICON_PATH_LIGHT = "src/assets/logos/Logo_White_Only.svg"
BAR_ICON_PATH_DARK = "src/assets/logos/Logo_Black_Only.svg"


# --- Settings page ---
class SP():
    '''
    Init class

    Parameters:
    page - flet page,
    nav_bar - navigation bar,
    settings_path - path to config,
    small logo and back button in app bar.
    '''
    def __init__(self, page, nav_bar, settings_path, back_button, small_logo):
        # --- Flet page ---
        self.page = page

        # --- Data containers ---
        self.small_logo = small_logo
        self.back_button = back_button
        self.nav_bar = nav_bar
        self.settings_path = settings_path

        # --- Initialization references ---
        self.theme_button = ft.Ref[ft.SegmentedButton]()
        self.language_button = ft.Ref[ft.SegmentedButton]()

        # --- Load config ---
        with open(self.settings_path, "r") as file:
            config = json.load(file)

        '''
        Creating the settings page

        Title, change of theme and language.
        '''
        self.content = ft.Row(
            ft.Column(
                [
                    ft.Text(
                        "Настройки / Settings", 
                        weight=ft.FontWeight.W_600,
                        size=17
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "Тема интерфейса / Interface theme", 
                                size=16
                            ),
                            ft.SegmentedButton(
                                selected_icon=ft.Icon(ft.Icons.CHECK),
                                selected=[config["theme"]],
                                allow_empty_selection=False,
                                segments=[
                                    ft.Segment(
                                        value="DARK",
                                        label=ft.Text("Тёмная / Dark"),
                                        icon=ft.Icons.DARK_MODE
                                    ),
                                    ft.Segment(
                                        value="LIGHT",
                                        label=ft.Text("Светлая / Light"),
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
                                "Язык интерфейса / Interface language", 
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
                                on_change=self.change_language,
                                ref=self.language_button
                            ),
                            ft.Text(
                                "Язык интерфейса изменится при перезагрузке приложения. / The interface language will change when the application is restarted.",
                                size=14,
                                width=300,
                                text_align=ft.TextAlign.JUSTIFY,
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
    
    '''
    Change theme

    Open the config file, change the theme, 
    write it to the file and change it in real time.
    '''
    def change_theme(self):
        with open(self.settings_path, "r") as file:
            config = json.load(file)
            config["theme"] = self.theme_button.current.selected[0]

        with open(self.settings_path, "w") as file:
            json.dump(config, file, indent=4)
        
        if self.theme_button.current.selected[0] == "DARK":
            self.page.theme_mode = ft.ThemeMode.DARK
            self.small_logo.current.src = BAR_ICON_PATH_LIGHT
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.small_logo.current.src = BAR_ICON_PATH_DARK
    
    '''
    Change language

    Open the config file, change the language, 
    write it to the file.
    '''
    def change_language(self):
        with open(self.settings_path, "r") as file:
            config = json.load(file)
            config["language"] = self.language_button.current.selected[0]

        with open(self.settings_path, "w") as file:
            json.dump(config, file, indent=4)