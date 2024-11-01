from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.screenmanager import SlideTransition


import youtubeDL
from youtubeDL import YouTubeDL as Youtube


class MainLayout(Screen):
    pass

class YoutubeLayout(Screen):  # Change to inherit from Screen
    def __init__(self, **kwargs):
        layout = BoxLayout(orientation='vertical')

        super(YoutubeLayout, self).__init__(**kwargs)
        



    def telecharge(self, instance):
            try:
                lien = self.ids.link.text
                yt = Youtube(lien)
                self.ids.image.source = str(yt.thumbnail)
                self.ids.MSG.text = f"Downloading: {yt.title}"
                
                yt.download()
                self.ids.MSG1.text = "Downloading: FINISH"
            except Exception as e:
                self.ids.MSG1.text = f"ERROR: {str(e)}"








class TiktokLayout(Screen):  # Change to inherit from Screen
    def __init__(self, **kwargs):
        super(TiktokLayout, self).__init__(**kwargs)
        self.add_widget(Label(text="TikTok Downloader", size_hint=(1, 0.3), font_size="30"))

class InstagramLayout(Screen):  # Change to inherit from Screen
    def __init__(self, **kwargs):
        super(InstagramLayout, self).__init__(**kwargs)
        self.add_widget(Label(text="Instagram Downloader", size_hint=(1, 0.3), font_size="30"))

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainLayout(name='main'))  # Main menu layout
        sm.add_widget(YoutubeLayout(name='youtube')) 
        sm.add_widget(TiktokLayout(name='tiktok')) 
        sm.add_widget(InstagramLayout(name='instagram')) 
        return sm

if __name__ == '__main__':
    MyApp().run()
