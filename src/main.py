import flet as ft


MAIN_ICON_DARK_PATH = "src/assets/logos/Logo_Main_Black.svg"
MAIN_ICON_LIGHT_PATH = "src/assets/logos/Logo_Main_White.svg"


def main(page: ft.Page):
    # --- App settings ---
    page.title = "Valgrind"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # --- Bottom bar ---
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.TEXT_FIELDS,
                label="Текст"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="Главная"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.IMAGE, 
                label="Изображение"
            )
        ],
        selected_index=1,
    )

    # --- Menu bar ---
    async def handle_change(e: ft.Event[ft.NavigationDrawer]):
        print(f"Selected Index changed: {e.control.selected_index}")
        print()
        await page.close_drawer()

    async def open_drawer():
        await page.show_drawer()
    
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.Icons.HOME, 
                label="Главная",
                
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.SETTINGS, label="Настройки"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.INFO, label="Справка"
            )
        ],
        on_change=handle_change,
        tile_padding=ft.Padding(top=10),
    )

    # -- Main info --
    main_info_page = ft.Row(
        [
            ft.Column(
                [
                    ft.Image(
                        src=MAIN_ICON_LIGHT_PATH if page.theme_mode.value == "dark" else MAIN_ICON_DARK_PATH,
                        width=300,
                        height=300
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

    page.add(
        ft.IconButton(
            on_click=open_drawer,
            icon=ft.Icons.MENU,
        ),
        main_info_page
    )


if __name__ == "__main__":
    ft.run(main)