import flet as ft
from Views.InicioView import InicioView

async def main(page: ft.Page):
    
    page.bgcolor = ft.colors.BLUE_200
    page.padding=0 # 
    page.title = "cuestionario"
    page.scroll = ft.ScrollMode.AUTO
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ventanda = InicioView(page)
    page.views.append(ventanda.getInicioView())
    await page.update_async()

ft.app(target=main,assets_dir="assets")


