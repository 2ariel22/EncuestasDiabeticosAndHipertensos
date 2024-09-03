import flet as ft
class Preguntas():

    def __init__(self,page: ft.Page):
        self.page = page
        self.listCuestions = {
            "pregunta1":ft.Text(value="¿Haz sido diagnosticado previamente?"),
            "pregunta2":"¿que?",
            "pregunta3":"",
            "pregunta4":"",
            "pregunta5":""
        
        }
        
        self.allRadioButtons = [
                ft.Radio(value="1", label="Si",visible=False),
                ft.Radio(value="0", label="No",visible=False),
                ft.Radio(value="0", label="No",visible=False),
                ft.Radio(value="0", label="No",visible=False),
                ft.Radio(value="0", label="No",visible=False)
            ]
        self.radioGrup = ft.RadioGroup(content=ft.Column(
            controls=self.allRadioButtons
        ),on_change=self.preguntaseleccionada)
    
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
        elif():
            print("huesoxd")
        
        
        
        

        self.page.update()


    def changeVradioButtons(self,radioButton, state):
        self.allRadioButtons[radioButton] = state
        self.page.update()

    def getPregunta1(self):
        #self.changeVradioButtons(0,True)
        #self.changeVradioButtons(0,True)
        
        firtsCuestion = ft.Column(controls=[
            self.listCuestions["pregunta1"],
            self.radioGrup
        ])          

        return firtsCuestion