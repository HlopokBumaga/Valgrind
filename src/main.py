import flet as ft
import json
from assets.pages.Pages import MP, TEP, IEP, SP

# --- Paths ---
MAIN_ICON_DARK_PATH = "src/assets/logos/Logo_Black_Only_Text.svg"
MAIN_ICON_LIGHT_PATH = "src/assets/logos/Logo_White_Only_Text.svg"
BAR_ICON_LIGHT_PATH = "src/assets/logos/Logo_White_Only.svg"
BAR_ICON_DARK_PATH = "src/assets/logos/Logo_Black_Only.svg"
CONFIG_PATH = "src/config.json"
LOCAL_PATH = "src/assets/localization/local_"

# --- Config ---
with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

# --- Load language vocabulary ---
with open(f"{LOCAL_PATH}{config["language"]}.json", "r") as local:
    LOCAL_DICT = json.load(local)


# --- App ---
def main(page: ft.Page):
    # --- App settings ---
    page.title = "Valgrind"

    if config["theme"] == "DARK":
        page.theme_mode = ft.ThemeMode.DARK
    else:
        page.theme_mode = ft.ThemeMode.LIGHT

    page.window.width = 500
    page.window.height = 700

    # --- Back button ---
    back_button = ft.Ref[ft.IconButton]()

    # --- Small logo ---
    small_logo = ft.Ref[ft.Image]()

    # --- Init pages ---
    main_page = MP(page, MAIN_ICON_LIGHT_PATH, MAIN_ICON_DARK_PATH, LOCAL_DICT)
    text_page = TEP(page, LOCAL_DICT)
    image_page = IEP(page)

    # --- Bottom bar ---
    def set_content(e):
        page.controls.clear()
        current_page = e.control.selected_index

        match current_page:
            case 0:
                page.add(
                    text_page.get_content()
                )
            case 1:
                page.add(
                    main_page.get_content()
                )
            case 2:
                page.add(
                    image_page.get_content()
                )
            
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.TEXT_FIELDS,
                label=LOCAL_DICT["navigation_bar"][0]
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label=LOCAL_DICT["navigation_bar"][1]
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.IMAGE_OUTLINED,
                selected_icon=ft.Icons.IMAGE,
                label=LOCAL_DICT["navigation_bar"][2]
            )
        ],
        on_change=set_content,
        selected_index=1,
        bgcolor=ft.Colors.SURFACE_CONTAINER
    )

    # --- Menu bar ---
    settings_page = SP(page, page.navigation_bar, back_button, CONFIG_PATH, small_logo, BAR_ICON_DARK_PATH, BAR_ICON_LIGHT_PATH)

    def back_page():
        page.controls.clear()
        page.navigation_bar.visible = True
        back_button.current.visible = False

        current_page = page.navigation_bar.selected_index

        match current_page:
            case 0:
                page.add(
                    text_page.get_content()
                )
            case 1:
                page.add(
                    main_page.get_content()
                )
            case 2:
                page.add(
                    image_page.get_content()
                )

    def load_settings_page():
        page.controls.clear()
        page.add(
            settings_page.get_content()
        )

    page.appbar = ft.AppBar(
        leading=ft.Image(
            src=BAR_ICON_LIGHT_PATH if page.theme_mode.value == "dark" else BAR_ICON_DARK_PATH,
            width=40,
            ref=small_logo
        ),
        actions=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                visible=False,
                on_click=back_page,
                ref=back_button
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon=ft.Icons.SETTINGS, 
                        content=LOCAL_DICT["app_bar"][0],
                        on_click=load_settings_page
                    ),
                    ft.PopupMenuItem(icon=ft.Icons.INFO, content=LOCAL_DICT["app_bar"][1]),
                ]
            ),
        ],
        title=ft.Text(
            "Valgrind"
        ),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER
    )

    # --- Start rendering ---
    page.add(
        main_page.get_content()
    )    

if __name__ == "__main__":
    ft.run(main)