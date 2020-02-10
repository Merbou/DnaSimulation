from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import sys

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '50')
Config.set('graphics', 'resizable', '0')


class motifWindow(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rand_msg()

    def rand_msg(self):
        """
        @params None
            view message  
        @return None
        """
        if (sys.argv[1] is  None):return

        if(sys.argv[2] != ""):
            msg = "position of motif \""+sys.argv[1]+"\" :"+sys.argv[2]
            self.__view_position(msg)
        else:
            msg = "motif is not exist"
            self.__view_position(msg)

    def __view_position(self, msg):
        """
        @parms string
        assignment the field 
        @return None
        """
        position_field = self.ids.position_field
        position_field.text += msg


class motifApp(App):
    def build(self):
        return motifWindow()


if __name__ == "__main__":
    motifApp().run()
