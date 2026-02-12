import flet as ft

# --- Paths ---
MAIN_ICON_DARK_PATH = "src/assets/logos/Logo_Main_Black.svg"
MAIN_ICON_LIGHT_PATH = "src/assets/logos/Logo_Main_White.svg"

# --- App ---
def main(page: ft.Page):
    # --- App settings ---
    page.title = "Valgrind"
    page.theme_mode = ft.ThemeMode.DARK

    # --- Menu bar ---
    async def handle_change(e: ft.Event[ft.NavigationDrawer]):
        print(f"Selected Index changed: {e.control.selected_index}")
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
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            on_click=open_drawer,
            icon=ft.Icons.MENU,
        ),
        leading_width=40,
        center_title=False,
    )

    # --- Bottom bar ---
    def set_content(e):
        page.controls.clear()
        current_page = e.control.selected_index

        match current_page:
            case 0:
                page.add(
                    text_encryption_page(page)
                )
            case 1:
                page.add(
                    main_page(page)
                )
            case 2:
                page.add(
                    image_encryption_page(page)
                )
            
    
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
        on_change=set_content,
        selected_index=1,
    )

    # --- Start rendering ---
    page.add(
        main_page(page)
    )

# --- Main page ---
def main_page(page):
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

    return main_info_page

# --- Text encryption page ---
def text_encryption_page(page):
    content = ft.Row(
        [
            ft.Column(
                [
                    ft.Text(value="Шифрование текста"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return content

# --- Image encryption page ---
def image_encryption_page(page):
    content = ft.Row(
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
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return content
    

if __name__ == "__main__":
    ft.run(main)