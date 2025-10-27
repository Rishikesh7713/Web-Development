from tkinter import*
win=Tk()
win.title("Age Calculator")
win.geometry("500x400")
frame=Frame(master=win,bg="white",height=300)
lbl1=Label(frame,text="Hey There! This is a Age Calculator")
lbl2=Label(frame,text="Enter your Birth Year")
ent=Entry(frame)

def display():
   yr=ent.get()
   yr=int(yr)
   res=Text("Your Age is : "+yr-2025)
   txt.insert(END,res)

txt=Text(bg="red",fg="white",height=20)
btn=Button(command=display,text="Press")

frame.pack()
lbl1.pack()
lbl2.pack()
ent.pack()
btn.pack()
txt.pack()
win.mainloop()