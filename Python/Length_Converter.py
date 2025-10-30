from tkinter import*
win=Tk()
win.title("Length Coverter")
win.geometry("500x400")
lbl1=Label(text="Hey There! This app Will convert mm to cm")
mm=Entry()
def dis():
    m=mm.get()
    res=int(m)/10
    txt.insert(END,int(res))

btn=Button(command=dis,text="Click")
txt=Text(bg="blue",fg="white")
lbl1.pack()
mm.pack()
btn.pack()
txt.pack()
win.mainloop()