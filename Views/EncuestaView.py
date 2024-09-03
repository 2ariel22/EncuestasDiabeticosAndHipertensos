import flet as ft
class EncuestaView():

    def __init__(self,page: ft.Page,navbar):
        self.page = page
        self.navBar = navbar
        self.pregunta1= ft.Text(value="¿Haz sido diagnosticado previamente?")
        self.medico1= ft.Text(value="Continue haciendo un seguimiento")
        self.medico2= ft.Text(value="Consulte inmediatamente a un especialista")
        self.radio1 =ft.Radio(value="1", label="Si")
        self.radio2 = ft.Radio(value="0", label="No")
        self.radio3 = ft.Radio(value="0", label="No",visible=False)
        self.radio4 = ft.Radio(value="0", label="No",visible=False)
        self.radio5 = ft.Radio(value="0", label="No",visible=False)
 

    def send(self,e):
        #vista = self.registroView.getRegisterView()
        #self.page.views.append(vista)
        #self.page.update()
        print("dates")
    def preguntaseleccionada(self,e: ft.ControlEvent):
        print(e.data)
        #only diabetico
        selection = int(e.data)
        #first cycle
        if(selection==1):
            #respuesta si el usurio selecciono si 
            self.pregunta1.value="¿Qué tipo de diabetes tienes?"
            self.radio1.label="Tipo 1" #respuesta
            self.radio2.label="Tipo 2"
            self.radio3.label="No estoy seguro" 
            self.radio3.visible=True
            self.radio1.value=3
            self.radio2.value=3
            self.radio3.value=3
            
        elif(selection==0):
            self.pregunta1.value="¿Has experimentado alguno de los siguientes síntomas recientemente? (selecciona todos los que apliquen)"
            self.radio1.label="Fatiga" 
            self.radio2.label="Orinar con frecuencia" 
            self.radio3.label="Sed excesiva"
            self.radio3.visible=True
            self.radio4.label="Vision borrosa"
            self.radio4.visible=True
            self.radio5.label="No he tenido ninguno"
            self.radio5.visible=True
            self.radio1.value=7
            self.radio2.value=7
            self.radio3.value=7
            self.radio4.value=7
            self.radio5.value=8

        elif(selection==3):
            #respuesta si el usurio selecciono si esta muchacha si sabe
            self.pregunta1.value="¿Estás siguiendo algún tratamiento actualmente?"
            self.radio1.label="Si" #respuesta
            self.radio2.label="No"
            self.radio3.visible=False
            self.radio1.value=5
            self.radio2.value=6

        elif(selection==5 ):
            self.pregunta1.value="¿Cuál es el tratamiento que sigues? (selecciona todos los que apliquen)"
            self.radio1.label="Insulina" #respuesta
            self.radio2.label="Medicamentos orales"
            self.radio3.label="Dieta"
            self.radio3.visible=True
            self.radio4.label="Ejercicios"
            self.radio4.visible=True
            self.radio5.label="Ninguno"
            self.radio5.visible=True
            self.radio1.value=8
            self.radio2.value=8
            self.radio3.value=8
            self.radio4.value=8
            self.radio5.value=6

        elif(selection==6):
            self.pregunta1.value="¿Por qué no estás siguiendo un tratamiento?"
            self.radio1.label="No lo creo necesario" #respuesta
            self.radio2.label="No puedo costearlo"
            self.radio3.label="No tengo acceso a medicamentos"
            self.radio3.visible=True
            self.radio4.label="Otro motivo"
            self.radio4.visible=True
            self.radio1.value=8
            self.radio2.value=8
            self.radio3.value=8
            self.radio4.value=8

        elif(selection==7):
            self.pregunta1.value="¿Con qué frecuencia has experimentado estos síntomas en las últimas semanas?"
            self.radio1.label="Diario" #respuesta
            self.radio2.label="A veces"
            self.radio3.label="Raramente"
            self.radio3.visible=True
            self.radio1.value=9
            self.radio2.value=9
            self.radio3.value=8
        
        elif(selection==8):
            self.pregunta1.value="¿Conoces tu nivel de glucosa en sangre en ayunas?"
            self.radio1.label="Si" #respuesta
            self.radio2.label="No"
            self.radio1.value=10
            self.radio2.value=11
            self.radio3.visible=False
            self.radio4.visible=False
            self.radio5.visible=False
        
        elif(selection==9):
            self.pregunta1.value="¿Has visitado a un médico recientemente debido a estos síntomas?"
            self.radio1.label="Si" #respuesta
            self.radio2.label="No"
            self.radio1.value=12
            self.radio2.value=13
            self.radio3.visible=False
            self.radio4.visible=False
            self.radio5.visible=False
        
        
        
        

        self.page.update()
    def getEncuestaHipertensoView(self):
        
        title = ft.Text(
            value="Encuesta Hipertenso",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )

        
                        
        pregunta1 = ft.Text(value="¿Haz sido diagnosticado previamente?")
        respuesta1 = ft.RadioGroup(content=ft.Column([
                        ft.Radio(value="1", label="Si"),
                        ft.Radio(value="0", label="No")]),on_change=self.preguntaseleccionada)
        firtsCuestion = ft.Column(controls=[
            pregunta1,
            respuesta1
        ])                

        prgunta2 = ft.Radio(
            label="pregunta2",
            helper_text="¿con que frecuencia juega futbol?",
            
        )
        cg = ft.RadioGroup(content=ft.Column([
                        ft.Radio(value="red", label="Red"),
                        ft.Radio(value="green", label="Green"),
                        ft.Radio(value="blue", label="Blue")]))
        send_button = ft.ElevatedButton(
            text="Enviar",
            on_click=self.send,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )


        # Contenedor principal centrado
        contente = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                 
                title,
                ft.Container(padding=10),
                firtsCuestion,
                ft.Container(padding=10),
                prgunta2,
                ft.Container(padding=20),
                send_button,
              
              
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

        # Contenedor resaltado en el centro
        return ft.View(
            route="/EncuestaDiabetico",
            controls=[
                ft.Stack(
                    [
                    background,
                    contenido,
                    self.navBar,
                   ]
                    ,width=self.page.width,
                    alignment=ft.alignment.center,
                    
                    )
                    ],
                    
                    padding=0,
                    scroll=ft.ScrollMode.AUTO,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    
        )
    
    def getEncuestaDiabeticoView(self):
        
        title = ft.Text(
            value="Encuesta Diabeticos",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )

    
        respuesta1 = ft.RadioGroup(content=ft.Column([
                        self.radio1,
                        self.radio2,
                        self.radio3,
                        self.radio4,
                        self.radio5]),on_change=self.preguntaseleccionada)
        firtsCuestion = ft.Column(controls=[
            self.pregunta1,
            respuesta1
        ])          
       


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

        # Contenedor resaltado en el centro
        return ft.View(
            route="/EncuestaHipertenso",
            controls=[
                ft.Stack(
                    [
                    background,
                    contenido,
                    self.navBar,
                   ]
                    ,width=self.page.width,
                    alignment=ft.alignment.center,
                    
                    )
                    ],
                    
                    padding=0,
                    scroll=ft.ScrollMode.AUTO,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    
        )