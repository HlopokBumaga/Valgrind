import flet as ft
from assets.pages.Pages import MP, TEP, IEP

# --- Paths ---
MAIN_ICON_DARK_PATH = "src/assets/logos/Logo_Black_Only_Text.svg"
MAIN_ICON_LIGHT_PATH = "src/assets/logos/Logo_White_Only_Text.svg"
BAR_ICON_LIGHT_PATH = "src/assets/logos/Logo_White_Only.svg"
BAR_ICON_DARK_PATH = "src/assets/logos/Logo_Black_Only.svg"

# --- App ---
def main(page: ft.Page):
    # --- App settings ---
    page.title = "Valgrind"
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- Init pages ---
    main_page = MP(page, MAIN_ICON_LIGHT_PATH, MAIN_ICON_DARK_PATH)
    text_page = TEP(page)
    image_page = IEP(page)

    # --- Menu bar ---
    page.appbar = ft.AppBar(
        leading=ft.Image(
            src=BAR_ICON_LIGHT_PATH if page.theme_mode.value == "dark" else BAR_ICON_DARK_PATH,
            width=40
        ),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(icon=ft.Icons.SETTINGS, content="Настройки"),
                    ft.PopupMenuItem(icon=ft.Icons.INFO, content="Справка"),
                ]
            ),
        ],
        title=ft.Text(
            "Valgrind"
        ),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER
    )

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
                label="Текст"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Главная"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.IMAGE_OUTLINED,
                selected_icon=ft.Icons.IMAGE,
                label="Изображение"
            )
        ],
        on_change=set_content,
        selected_index=1,
        bgcolor=ft.Colors.SURFACE_CONTAINER
    )

    # --- Start rendering ---
    page.add(
        main_page.get_content()
    )
    

if __name__ == "__main__":
    ft.run(main)