'''
Valgrind | GuidePage.py

Creating the guide page.
'''

import flet as ft
import asyncio


# --- Guide page ---
class GP():
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

        # --- Init guides ---
        with open("assets/methods/guides/how_ru.md", "r") as how_file:
            how_data = how_file.readlines()


        self.content = ft.Tabs(
            selected_index=0,
            length=3,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.TabBar(
                        tabs=[
                            ft.Tab(
                                label="Шифрование данных", 
                                icon=ft.Icons.QUESTION_MARK
                            ),
                            ft.Tab(
                                label="Методы шифрования", 
                                icon=ft.Icons.LIST
                            ),
                            ft.Tab(
                                label="О программе", 
                                icon=ft.Icons.INFO_OUTLINE,    
                            ),
                        ],
                        tab_alignment=ft.TabAlignment.CENTER
                    ),
                    ft.TabBarView(
                        expand=True,
                        controls=[
                            ft.Column(
                                controls = [
                                    ft.Markdown(
                                        value="".join(how_data),
                                        selectable=True,
                                        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                                    ),
                                ],
                                scroll=ft.ScrollMode.AUTO
                            ),
                            ft.Container(
                                content=ft.Text("Methods"),
                                alignment=ft.Alignment.CENTER,
                            ),
                            ft.Container(
                                content=ft.Text("About"),
                                alignment=ft.Alignment.CENTER,
                            )
                        ],
                    ),
                ]
            )
        
        )
                


        self.GuideAppBar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda: asyncio.create_task(self.page.push_route("/")),
            ),
            title=ft.Text(self.local["app_bar"][1]),
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER,
        )


    
    def get_content(self):
        return self.content