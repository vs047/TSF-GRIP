from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
class app:
    def __init__(self):
        self.window=Tk()
        self.window.title("Score Identifier")
        self.window.geometry('500x350')
        self.window.resizable(False,False)
        self.icon=PhotoImage(file="images/logo.png")
        self.background=PhotoImage(file='images/background.png')
        self.window.iconphoto(True,self.icon)
        self.canvas=Canvas(self.window,width=500,height=350)
        self.canvas.pack()
        self.canvas.create_image(0,0,anchor=NW,image=self.background)
        Label(self.window,text='Score Identifier',fg='blue',bg='brown',font=('Arieal',30)).place(relx=0.2,rely=0.05)
        Label(self.window,text='Enter working Hour per day',fg='blue',bg='brown',font=('Arieal',10)).place(rely=0.3)
        self.hour=DoubleVar()
        Entry(self.window,text=self.hour,font=('Arieal',10)).place(relx=0.4,rely=0.3)
        Button(self.window,text='Show Output',bg='blue',fg='brown',font=('Arieal',20),command=self.generate).place(relx=0.25,rely=0.55)
        self.window.mainloop()
    def generate(self):
        if self.hour.get()<0 and self.hour.get()>24:
            messagebox.showerror("Error","Invalid Hours")
        else:
            data=pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')
            x=data[['Hours']]
            y=data[['Scores']]
            x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.25)
            model=LinearRegression()
            model.fit(x_train,y_train)
            score=model.predict([[self.hour.get()]])
            messagebox.showinfo("Information","Score is = {}".format(score[0,0]))
    
sample=app()
