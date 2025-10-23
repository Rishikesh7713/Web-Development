from tkinter import*
win=Tk()
win.title=("Login app")
win.geometry('500x400')
frame=Frame(master=win,bg="grey",height=200,width=700)
lbl1=Label(frame,text="Enter the Full Name",bg="blue",fg="white",width=12)
lbl2=Label(frame,text="Enter your Email ID",bg="blue",fg="white",width=12)
lbl3=Label(frame,text="Enter Your Password",bg="blue",fg="white",width=12)
ent1=Entry(frame)
ent2=Entry(frame)
ent3=Entry(frame,show="*")

def display():
    name=ent1.get()
    greet="Hey "+name+" How are you?"
    mes="\n Congrats for your new Account"
    txt.insert(END,greet)
    txt.insert(END,mes)

txt=Text(bg="brown",fg="white",height=20)
btn=Button(text="Create Account",command=display,bg="black",fg="white")

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
ent1.place(x=150,y=20)
lbl2.place(x=20,y=80)
ent2.place(x=150,y=80)
lbl3.place(x=20,y=140)
ent3.place(x=150,y=140)
btn.place(x=200,y=220)
txt.place(x=60,y=300)
win.mainloop()