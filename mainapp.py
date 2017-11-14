from kivy.app import App
#kivy.require("1.10.0")

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen , FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from musicFile import MusicFileInfo


class OtherScreen(Screen):
    def __init__(self, **kwargs):
        # constructor to intialize labels for the artist screen in the app
        super(OtherScreen,self).__init__(**kwargs)
        # get music files
        self.gmf = MusicFileInfo()
        musiclist , musiclen = self.gmf.getMusic()
        self.create_Labels(musiclist , musiclen)

    def printinfo(self, instance, value):
        # function that will be used to send user to music player when the
        # press tag
        # currently used for testing to ensure it works
        print("User clicked on", value)

    def create_Labels(self, finfo,  numbuttons):
        # take in the number of labels to make
        # create that number of labels in a grid layout -> scrollview
        layout = GridLayout(cols=1, spacing=2,size_hint_y=None)
        layout.bind(minimum_height= layout.setter('height'))

        for i in finfo:
            print("Label name is " , i['id'])
            widget = Label(text="[ref=%s] %s [/ref] " % (i['song'],i['song']) , markup=True , size_hint_y=None )
            widget.bind(on_ref_press=self.printinfo)
            layout.add_widget(widget)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        self.add_widget(root)



class MainScreen(Screen):

    # function to handle login information
    def getlogininfo(self , login , password):
        # functin reads in the login and password input
        # print statements used for testing to ensure we are getting values
        # correctly
        # if info is correct go to next screen
        print(login)
        print(password)
        self.manager.transition = FadeTransition()
        self.manager.current = 'artist'


    def get_id(self , instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def PressBtn(self, instance):
        instance.parent.ids.text = self.get_id(instance)

    def callback(self , instance):
        # this function will be used to validate user
        # will create a seperate private class that will aunthenticate user
        # using for testing to ensure buttons work correctly
        if instance.text == 'Sign Up':
            if instance.state == 'down':
                print(instance.state)
                return
        else:

            print('The button is being pressed',  instance.id)

class AnotherScreen(Screen):
    # this screen will be the music player and will play , stop , skip the
    # music that is passed in
    # music will be gathered from server at this point
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("mainapp.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
