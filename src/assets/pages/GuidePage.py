'''
Valgrind | GuidePage.py

Creating the guide page.
'''

import flet as ft
import asyncio

# --- Paths ---
MAIN_ICON_PATH_DARK = "assets/logos/Logo_Main_Black.svg"
MAIN_ICON_PATH_LIGHT = "assets/logos/Logo_Main_White.svg"


# --- Guide page ---
class GP():
    '''
    Init class

    Parameters:
    page - flet page,
    local - localization vocabulary.
    '''
    def __init__(self, page, local, language):
        # --- Flet page ---
        self.page = page

        # --- Language vocabulary ---
        self.local = local

        # --- Initialization references ---
        self.main_logo = ft.Ref[ft.Image]()

        # --- Init guides ---
        with open(f"assets/methods/guides/how_{language}.md", "r") as how_file:
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
                                label=self.local["guide_page"][0], 
                                icon=ft.Icons.QUESTION_MARK
                            ),
                            ft.Tab(
                                label=self.local["guide_page"][1], 
                                icon=ft.Icons.LIST
                            ),
                            ft.Tab(
                                label=self.local["guide_page"][2], 
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
                            ft.Row(
                                ft.Column(
                                    [
                                        ft.Image(
                                            src=self.set_logo_by_theme(), width=250, ref=self.main_logo
                                        ),
                                        ft.Text(
                                            value=self.local["guide_page"][3],
                                            size=17,
                                            weight=ft.FontWeight.W_600,
                                            text_align=ft.TextAlign.CENTER
                                        ),
                                        ft.Text(
                                            value=self.local["guide_page"][4],
                                            size=17,
                                        ),
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan(
                                                    self.local["guide_page"][5],
                                                    ft.TextStyle(
                                                        decoration=ft.TextDecoration.UNDERLINE,
                                                        color=ft.Colors.BLUE_500,
                                                        decoration_color=ft.Colors.BLUE_500,
                                                        size=17
                                                    ),
                                                    on_click=lambda: asyncio.create_task(self.page.launch_url('https://github.com/HlopokBumaga/Valgrind')),
                                                ),
                                            ]
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    scroll=ft.ScrollMode.AUTO
                                ),
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
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
        self.main_logo.current.src = self.set_logo_by_theme()

        return self.content
    
    def set_logo_by_theme(self):
        if self.page.theme_mode.value == "dark":
            return MAIN_ICON_PATH_LIGHT
        else:
            return MAIN_ICON_PATH_DARK