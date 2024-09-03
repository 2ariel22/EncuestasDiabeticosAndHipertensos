import flet as ft
from Modelo.Preguntas import Preguntas
class EncuestaDiabeticos():

    def __init__(self,page: ft.Page,navbar):
        self.page = page
        self.navBar = navbar
        self.preguntas = Preguntas(page)
        
 
    def send(self,e):
        #vista = self.registroView.getRegisterView()
        #self.page.views.append(vista)
        #self.page.update()
        print("dates")


    def getEncuestaDiabeticoView(self):  
        title = ft.Text(
            value="Encuesta Diabeticos",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )

    
        firtsCuestion =  self.preguntas.getPregunta1()
       


        # Contenedor principal centrado
        contente = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                 
                title,
                ft.Container(padding=10),
                firtsCuestion,
                ft.Container(padding=20),
               
              
              
            ],
            width=300,
            expand=1
            
                
        )
        login = ft.Row(controls=[
            ft.Container(content=contente,
            padding=20,
            bgcolor='#5ce5ff',
            border_radius=80,
            margin=ft.margin.only(top=100),
            
            width=300,
            alignment=ft.alignment.center
        )
        ])

        
        background = ft.Container(
            width=self.page.width,
            height=self.page.height,
            bgcolor='#9ff2ff',
            alignment=ft.alignment.center,
            padding=0,
            margin=0
        )

        contenido = ft.Row(controls=[ft.Container(expand=1),login,ft.Container(expand=1),
        ],  

            
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            
        )
        print("todo bien aqui")

        return ft.View(
            route="/EncuestaDiabeticos",
            controls=[
                ft.Stack(
                    [
                    background,
                    self.navBar,
                    contenido,
                   ]
                    ,width=self.page.width,
                    
                    
                    )
                    ],
                    
                    padding=0,
                    scroll=ft.ScrollMode.AUTO,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    
        )