from tkinter import *
from tkinter import messagebox as mb


win = Tk()

mylabel = Label(win,text="明日の晩飯は？")
mylabel.pack()

text = Entry(win)
text.pack()
text.insert(END,"")

def ok_click():
    a = text.get()
    mb.showinfo("明日は", a + "を食べにいこか")
    
okButton = Button(win,text = "どうする？",command=ok_click)
okButton.pack()

win.mainloop()