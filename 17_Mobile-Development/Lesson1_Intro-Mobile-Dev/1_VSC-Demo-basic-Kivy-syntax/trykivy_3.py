from kivy.app import App
from kivy.uix.button import Button # button
from kivy.uix.label import Label # label
from kivy.uix.boxlayout import BoxLayout # layout (it's a widget too!)

class MyApp(App):
   def build(self):
      # when creating a widget, you can set the values of its properties.
      # Widget constructors only accept named parameters!
      txt = Label(text='This is a label') 
      btn = Button(text='This is a button')
      layout = BoxLayout()
      layout.add_widget(txt)
      layout.add_widget(btn)
      return layout # returns a widget that
                    # controls the layout of its children - buttons and labels

MyApp().run()