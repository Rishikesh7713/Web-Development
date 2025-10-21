from tkinter import*
win=Tk()
win.title("First Window in Tkinter")
win.geometry('1000x900')
lbl=Label(text="Hey There!",fg="White",bg="red",height=5,width=300)
albl=Label(text="Enter 2 Numbers to multiply",bg="brown")
no1=Entry()
no2=Entry()
sign=Label(text="x",fg="black",bg="red",height=5,width=300)
oans=Label(text="",fg="black",bg="red",height=5,width=300)

def display():
    n1=int(no1.get())
    n2 = int(no2.get())
  
    result=n1*n2
    oans.config(text=f"The result is: {result}")

btn=Button(text="Start",command=display,bg="green")
lbl.pack()
albl.pack()
no1.pack()
sign.pack()
no2.pack()
btn.pack()
oans.pack()
win.mainloop()