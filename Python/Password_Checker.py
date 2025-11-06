from tkinter import*
from tkinter import messagebox
win=Tk()
win.title("Password Strength Checker App")
win.geometry("500x400")
lbl1=Label(text="Hey There!",bg="green",fg="white")
lbl2=Label(text="This App will check your Password Strength based on the Length of your Password",bg="green",fg="white")
l=Label(text="Enter your Password",bg="red",fg="green")
ent=Entry()

def dis():
    passw=ent.get()
    p=len(passw)
    if p<5:
        messagebox.showwarning("Your Password is so simple. Enter more than 5 characters.")
    if p>5 and p<10:
        messagebox.showinfo("Your Password is Perfect!")
    if p>10:
        messagebox.showwarning("Your password cannot exceed more than 10 Characters!")

btn=Button(command=dis,text="Check Strength",bg="green",fg="red")
lbl1.pack()
lbl2.pack()
l.pack()
ent.pack()
btn.pack()
win.mainloop()