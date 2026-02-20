'''
Valgrind | Alpha ver. 1.0.0 | main.py

Application creation, window parameters are set.
Basic application elements are created: navigation bar, app bar.

---

Importing flet, json, and page classes:
MP - Main page
TEP - Text encryption page
IEP - Image encryption page
SP - Settings page
'''

import flet as ft
import json
from assets.pages.MainPage import MP
from assets.pages.ImagePage import IEP
from assets.pages.SettingsPage import SP
from assets.pages.TextPage import TEP

# --- Paths ---
MAIN_ICON_PATH_DARK = "assets/logos/Logo_Black_Only_Text.svg"
MAIN_ICON_PATH_LIGHT = "assets/logos/Logo_White_Only_Text.svg"
BAR_ICON_PATH_LIGHT = "assets/logos/Logo_White_Only.svg"
BAR_ICON_PATH_DARK = "assets/logos/Logo_Black_Only.svg"
CONFIG_PATH = "config.json"
LOCAL_PATH = "assets/localization/local_"

'''
Preloading config for further 
initial configuration of the application.
'''
with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

'''
Preloading the language vocabulary, 
depending on the language settings.

Contstruction: LOCAL[<chapter>][<index>]
- this is loading a phrase from the current language set. 
It is found further along the code and in Pages.
'''
with open(f"{LOCAL_PATH}{config['language']}.json", "r", encoding="utf-8") as file:
    LOCAL = json.load(file)


# --- Application ---
def main(page: ft.Page):
    '''
    Application configuration

    Setting the name, theme,
    and size of the application window.
    '''
    page.title = "Valgrind"

    if config["theme"] == "DARK":
        page.theme_mode = ft.ThemeMode.DARK
    else:
        page.theme_mode = ft.ThemeMode.LIGHT

    page.window.width = 500
    page.window.height = 700

    '''
    Init pages

    Initialization of classes: 
    main page, text encryption page, images.
    '''
    main_page = MP(page, LOCAL)
    text_page = TEP(page, LOCAL)
    image_page = IEP()

    '''
    Initialization references

    Small logo and back button in app bar.
    '''
    back_button_ref = ft.Ref[ft.IconButton]()
    small_logo_ref = ft.Ref[ft.Image]()

    '''
    Bottom bar

    Initializing the bottom bar and the click handler.
    '''
    def load_main_pages(e):
        page.controls.clear()
        current_page = e.control.selected_index

        match current_page:
            case 0:
                page.add(text_page.get_content())
            case 1:
                page.add(main_page.get_content())
            case 2:
                page.add(image_page.get_content())

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.TEXT_FIELDS, label=LOCAL["navigation_bar"][0]
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label=LOCAL["navigation_bar"][1],
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.IMAGE_OUTLINED,
                selected_icon=ft.Icons.IMAGE,
                label=LOCAL["navigation_bar"][2],
            ),
        ],
        on_change=load_main_pages,
        selected_index=1,
        bgcolor=ft.Colors.SURFACE_CONTAINER,
    )

    '''
    Menu bar

    Initialization of the app bar and 
    the handler for pressing the "back" button.

    ---

    Initialization of class:
    settings page.
    '''
    settings_page = SP(
        page,
        page.navigation_bar,
        CONFIG_PATH,
        back_button_ref,
        small_logo_ref
    )

    def back_to_main_page():
        page.controls.clear()
        page.navigation_bar.visible = True
        back_button_ref.current.visible = False

        current_page = page.navigation_bar.selected_index

        match current_page:
            case 0:
                page.add(text_page.get_content())
            case 1:
                page.add(main_page.get_content())
            case 2:
                page.add(image_page.get_content())

    def load_settings_page():
        page.controls.clear()
        page.add(settings_page.get_content())

    page.appbar = ft.AppBar(
        leading=ft.Image(
            src=(
                BAR_ICON_PATH_LIGHT
                if page.theme_mode.value == "dark"
                else BAR_ICON_PATH_DARK
            ),
            width=40,
            ref=small_logo_ref,
        ),
        actions=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                visible=False,
                on_click=back_to_main_page,
                ref=back_button_ref,
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon=ft.Icons.SETTINGS,
                        content=LOCAL["app_bar"][0],
                        on_click=load_settings_page,
                    ),
                    ft.PopupMenuItem(icon=ft.Icons.INFO, content=LOCAL["app_bar"][1]),
                ]
            ),
        ],
        title=ft.Text("Valgrind"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER,
    )

    # --- Start rendering ---
    page.add(main_page.get_content())


if __name__ == "__main__":
    ft.run(main)