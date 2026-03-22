'''
Valgrind | Beta ver. 2.0.0 | main.py

Application creation, window parameters are set.
Basic application elements are created: navigation bar, app bar.

---

Importing flet, json, and page classes:
MP - Main page
EP - Encryption page
DP - Decryption page
SP - Settings page
GP - Guide page
DE - Details page
'''

import flet as ft
import json
import asyncio
from assets.pages.MainPage import MP
from assets.pages.DecryptionPage import DP
from assets.pages.SettingsPage import SP
from assets.pages.EncryptionPage import EP
from assets.pages.GuidePage import GP
from assets.pages.Details import DE

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
    Initialization references

    Small logo in app bar.
    '''
    small_logo_ref = ft.Ref[ft.Image]()

    '''
    Init pages

    Initialization of classes: 
    main page, encryption page, decryption page and settings.
    '''
    main_page = MP(page, LOCAL)
    encryption_page = EP(page, LOCAL)
    decryption_page = DP(page, LOCAL)
    settings_page = SP(
        page,
        LOCAL,
        page.navigation_bar,
        CONFIG_PATH,
        small_logo_ref
    )
    guide_page = GP(page, LOCAL, config["language"])
    details_page = DE(page, LOCAL)

    '''
    Menu bar
    '''  
    MainAppBar = ft.AppBar(
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
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon=ft.Icons.SETTINGS,
                        content=LOCAL["app_bar"][0],
                        on_click=lambda: asyncio.create_task(page.push_route("/settings"))
                    ),
                    ft.PopupMenuItem(
                        icon=ft.Icons.INFO, 
                        content=LOCAL["app_bar"][1],
                        on_click=lambda: asyncio.create_task(page.push_route("/guide"))
                    ),
                ]
            ),
        ],
        title=ft.Text("Valgrind"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER,
    )

    BottomAppBar = ft.BottomAppBar(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.IconButton(
                    icon=ft.Icons.LOCK,
                    on_click=lambda: asyncio.create_task(page.push_route("/encryption"))
                ),
                ft.IconButton(
                    icon=ft.Icons.NO_ENCRYPTION_GMAILERRORRED,
                    on_click=lambda: asyncio.create_task(page.push_route("/decryption"))
                ),
            ],
        ),
        bgcolor=ft.Colors.SURFACE_CONTAINER,
    )

    '''
    Change route

    Allows you to switch between pages:
    / - Main page
    /encryption - Encryption page
    /decryption - Decryption page
    /settings - Settings page
    /guide - Guide page
    /details - Details page
    '''
    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    main_page.get_content()
                ],
                appbar=MainAppBar,
                bottom_appbar=BottomAppBar
            )
        )
        if page.route == "/settings":
            page.views.append(
                ft.View(
                    route="/settings",
                    controls=[
                        settings_page.get_content()
                    ],
                    appbar=settings_page.SettingsAppBar
                )
            )
        if page.route == "/encryption":
            page.views.append(
                ft.View(
                    route="/encryption",
                    controls=[
                        encryption_page.get_content()
                    ],
                    appbar=encryption_page.EncryptionAppBar
                )
            )
        if page.route == "/decryption":
            page.views.append(
                ft.View(
                    route="/decryption",
                    controls=[
                        decryption_page.get_content()
                    ],
                    appbar=decryption_page.DecryptionAppBar
                )
            )
        if page.route == "/guide":
            page.views.append(
                ft.View(
                    route="/guide",
                    controls=[
                        guide_page.get_content()
                    ],
                    appbar=guide_page.GuideAppBar
                )
            )
        if page.route == "/details":
            page.views.append(
                ft.View(
                    route="/details",
                    controls=[
                        details_page.get_content(
                            encryption_page.method.current.value, 
                            encryption_page.data.current.value, 
                            encryption_page.password.current.value
                        )
                    ],
                    appbar=details_page.DetailsAppBar
                )
            )
        page.update()
    
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # --- Start rendering ---
    route_change()


if __name__ == "__main__":
    ft.run(main)