from ruffier import test
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 

name = ''
age = 7

class InstrSCR(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        instr = Label(text = txt_instruction)
        
        h1BoxLayout = BoxLayout(size_hint = (0.8, None), height = '30sp')
        h2BoxLayout = BoxLayout(size_hint = (0.8, None), height = '30sp')
        
        HL1 = Label(text = "Введіть ім'я: ")
        self.in_name = TextInput(multiline = False)
        h1BoxLayout.add_widget(HL1)
        h1BoxLayout.add_widget(self.in_name)
        
        HL2 = Label(text = "Введіть вік: ")
        self.in_age = TextInput(text = '7', multiline = False)
        h2BoxLayout.add_widget(HL2)
        h2BoxLayout.add_widget(self.in_age)

        self.Button1 = Button(text = 'Почати', size_hint = (0.3, 0.2), pos_hint = {'center_x': 0.5})
        self.Button1.on_press = self.next

        v1BoxLayout = BoxLayout(orientation = "vertical", padding = 8, spacing = 8 )

        v1BoxLayout.add_widget(instr)
        v1BoxLayout.add_widget(h1BoxLayout)
        v1BoxLayout.add_widget(h2BoxLayout)
        v1BoxLayout.add_widget(self.Button1 )

        self.add_widget(v1BoxLayout)

    def next(self):
        global name, age
        name = self.in_name.text
        if not name:
            name = "user"
        try:
            age = int(self.in_age.text)
            #self.manager.current = ''
        except:
            self.in_age.text = "input Error"
        

        
        
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrSCR(name = 'instr'))

        return sm
app = HeartCheck()
app.run()