from ruffier import test
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
class InstrSCR(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrSCR(name = 'instr'))

        return sm
app = HeartCheck()
app.run()