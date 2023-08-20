from ruffier import test
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from Seconds import Second


class InstrSCR(Screen):
    def __init__(self, mainLableText, lable1Text, lable2Text, **kwargs):
        super().__init__(**kwargs)
        
        instr = Label(text = mainLableText)
        
        h1BoxLayout = BoxLayout(size_hint = (0.8, None), height = '30sp')
        h2BoxLayout = BoxLayout(size_hint = (0.8, None), height = '30sp')

        
        HL1 = Label(text = lable1Text)
        self.in_name = TextInput(multiline = False)
        h1BoxLayout.add_widget(HL1)
        h1BoxLayout.add_widget(self.in_name)
        
        HL2 = Label(text = lable2Text)
        if kwargs['name'] == 'instr': min_age = '7'
        else: min_age = ''
        self.in_age = TextInput(text = min_age, multiline = False)
        h2BoxLayout.add_widget(HL2)
        h2BoxLayout.add_widget(self.in_age)

        self.Button = Button(text = 'Почати', size_hint = (0.3, 0.2), pos_hint = {'center_x': 0.5})
        if kwargs['name'] == 'instr':
            self.Button.on_press = self.next_start
        else:
            self.Button.on_press = self.act_I

        if kwargs['name'] == 'pulsescr2':
            self.in_name.set_disabled(True)
            self.in_age.set_disabled(True)
            self.timer = Second(SMALL_TIME)

        vBoxLayout = BoxLayout(orientation = "vertical", padding = 8, spacing = 8 )

        vBoxLayout.add_widget(instr)
        if kwargs['name'] == 'pulsescr2': vBoxLayout.add_widget(self.timer)
        vBoxLayout.add_widget(h1BoxLayout)
        vBoxLayout.add_widget(h2BoxLayout)
        vBoxLayout.add_widget(self.Button)


        self.add_widget(vBoxLayout)

    def next_start(self):
        global name, age
        name = self.in_name.text
        if not name:
            name = "user"
        try:
            age = int(self.in_age.text)
            self.manager.current = 'pulsescr'
        except:
            self.in_age.text = "input Error"
    
    def timer_start(self):
        self.timer.start()
        self.Button.set_disabled(True)

    def timer_act_I(self, obj, finished):
        self.Button.set_disabled(False)
        self.in_name.set_disabled(False)
        self.Button.on_press = self.act_II

    def timer_act_II(self, obj, finished):
        self.Button.set_disabled(False)
        self.Button.on_press = self.act_III
    
    def timer_act_III(self, obj, finished):
        self.Button.set_disabled(False)
        self.in_age.set_disabled(False)
        self.Button.on_press = self.next_end

    def act_I(self):
        self.timer.bind(finished = self.timer_act_I)
        self.timer.start()
        self.Button.text = 'Продовжити'
    
    def act_II(self):
        global P2
        try:
            P2 = int(self.in_name.text)
            self.timer = Second(BIG_TIME - SMALL_TIME)
            self.timer.bind(finished = self.timer_act_II)
            self.timer.start()
            self.in_name.set_disabled(True)
            self.Button.set_disabled(True)
        except:
            self.in_name.text = "input Error"

    def act_III(self):
        self.timer = Second(SMALL_TIME)
        self.timer.bind(finished = self.timer_act_III)
        self.timer.start()
        self.Button.set_disabled(True)


    def next_end(self):
        global P3
        try:
            P3 = int(self.in_age.text)
            self.manager.current = 'result'
        except:
            self.in_age.text = "input Error"
