import flet as ft


def main(page: ft.Page):
    page.title = "Valgrind"

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.INFO
    )

    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.TEXT_FIELDS,
                label="Текст"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.IMAGE, 
                label="Изображение"
            )
        ],
        selected_index=None,
    )

if __name__ == "__main__":
    ft.run(main)