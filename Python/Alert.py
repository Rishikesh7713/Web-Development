from tkinter import*
from tkinter import messagebox
win=Tk()

def alert():
    messagebox.showwarning("Alert","Virus Detected")

btn=Button(text="Scan for Viruses",command=alert)
btn.place(x=40,y=30)
win.mainloop()