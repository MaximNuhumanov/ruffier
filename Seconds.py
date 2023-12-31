from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty



class Second(Label):
    
    finished = BooleanProperty(False)
    
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        self.finished = False
        my_text = 'Пройшло секунд: ' + str(self.current)
        super().__init__(text = my_text, **kwargs)

    def start(self):
        Clock.schedule_interval(self.change, 1)
        
    def change(self, dt):
        self.current += 1
        self.text = 'Пройшло секунд: ' + str(self.current)
        if self.current >= self.total:
            self.finished = True
            return False