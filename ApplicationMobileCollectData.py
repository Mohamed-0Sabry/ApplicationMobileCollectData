import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Childapp(GridLayout):
    def __init__(self, **kwargs):
        super(Childapp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = "STUDENT NAME :"))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text = "STUDENT MARKS :"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text = "STUDENT GENDER"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.add_widget(Label(text = " I love UOU"))
        self.s_lol = TextInput()
        self.add_widget(self.s_lol)

        self.press = Button(text = "Click Me!")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):  
        print("Student Name :" + self.s_name.text)
        print("Studnt Marks :" + self.s_marks.text)
        print("Student Genger :" + self.s_gender.text)
        print("\n")

class ParrentApp(App):
    def build(self):
        return Childapp()
    
if __name__ == "__main__":
    ParrentApp().run()