import mysql.connector as sql
from kivy.app import App 
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size=(370,600)
Window.clearcolor=(100/255.0,0,2,1)

class Employeer(App):
    def build(self):
        self.title=("employee")
        layout=GridLayout(cols=1)
        submit=Button(text="add employee",on_press=self.sub)
        self.username=TextInput(hint_text="username",multiline=False,
                                size_hint=(0.1,0.3))
        self.work=TextInput(text="work",multiline=False,
                            size_hint=(0.1,0.3))
        self.phone=TextInput(text="phone",multiline=False,
                             size_hint=(0.1,0.3))
        self.country=TextInput(text="country",multiline=False,
                               size_hint=(0.1,0.3))
        self.gender=TextInput(text="gender",multiline=False,
                              size_hint=(0.1,0.3))
        self.imo=Image(source="login.png")
        self.L1=Label(text="emloyee")
        self.L2=Label(text="add new emplyee")
        layout.add_widget(self.imo)
        layout.add_widget(self.L1)
        layout.add_widget(self.L2)
        layout.add_widget(self.username)
        layout.add_widget(self.work)
        layout.add_widget(self.phone)
        layout.add_widget(self.country)
        layout.add_widget(self.gender)
        layout.add_widget(submit)

        return layout
    def sub(self,event):
        un=self.username.text
        wo=self.work.text
        ph=self.phone.text
        co=self.country.text
        gn=self.gender.text
        con=sql.connect(host="localhost",user="root",password="",database="kivo")
        cur=con.cursor()
        query='Insert Into users(username,work,phone,country,gender)values(%s,%s,%s,%s,%s)'
        val=(un,wo,ph,co,gn)
        cur.execute(query,val)
        con.commit()
        con.close()
if __name__ =="__main__":
    Employeer().run()
