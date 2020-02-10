
from model import adn as a
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from subprocess import Popen, PIPE

### init panel
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', '0')


class LoadDialog(FloatLayout):

    # Class for widget loadFile

    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class menuWindow(BoxLayout):

    # Class for menu widget

    def __init__(self, **kwargs):
        # init all attributes
        super().__init__(**kwargs)

    def dismiss_popup(self):
        # cancel panel of filechooser
        self._popup.dismiss()

    def show_load(self):
        # Create&Show  panel of filechooser

        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)

        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        """
        @params string,string
        start a schedule home.py with path of file
        @return None
        """
        Popen(['python', "home.py", filename[0], "path"],
              stdout=PIPE, stderr=PIPE)

    def chooseFunction(self):
        """
        @params None
        start a schedule home.py with size of DNA
        @return None
        """
        # get object of field test
        dna_size_field = self.ids.dna_size_field
        size = dna_size_field.text

        Popen(['python', "home.py", size, "size"], stdout=PIPE, stderr=PIPE)


class menuApp(App):
    ## build a panel from operating system
    def build(self):
        return menuWindow()


if __name__ == "__main__":
    ##View Window
    menuApp().run()
