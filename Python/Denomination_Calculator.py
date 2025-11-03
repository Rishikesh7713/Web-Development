from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
win=Tk()
win.geometry=("700x600")
win.title("Denomination Calculator")
win.configure(bg="green")
upload=Image.open("money.jpg")
upload=upload.resize((300,300))
img=ImageTk.PhotoImage(upload)
lbl=Label(win,image=img,bg="light blue")
lbl.place(x=120,y=80)
lbl1=Label(win,text="Hey There! This is a Denomination Calculator",bg="light blue")
lbl1.place(relx=0.5,y=350)

def msg():
    msgbox=messagebox.showinfo("Alert! Do you want to Calculate the Denomination?")
    if msgbox=="ok":
        topwin()

btn=Button(win,command=msg,text="Let's go!")
btn.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.geometry=("700x600")
    top.title("This is Top Level")
    top.configure(bg="green")
    lbl=Label(top,text="Enter your Amount",image=img,bg="light blue")
    ent1=Entry(top)
    lbl=Label(top,text="Here are the no of Amount")
    lbl1=Label(top,text="2000")
    lbl2=Label(top,text="500")
    lbl3=Label(top,text="100")
    en1=Entry(top)
    en2=Entry(top)
    en3=Entry(top)

    def calculate():
        try:
            global am
            am=int(ent1.get())
            n2000=am//2000
            am%=2000
            n500=am//500
            am%=500
            n100=am//100
            am%=100

            en1.delete(0,END)
            en2.delete(0,END)
            en3.delete(0,END)

            en1.insert(END,str(n2000))
            en2.insert(END,str(n500))
            en3.insert(END,str(n100))

        
        except ValueError:
            messagebox.showerror("Please enter a Valid info!")


    bt=Button(top,command=calculate)
    lbl.place(x=240,y=50)
    ent1.place(x=200,y=80)
    lbl1.place(x=170,y=200)
    lbl2.place(x=170,y=230)
    lbl3.place(x=170,y=250)
    en1.place(x=200,y=200)
    en2.place(x=200,y=230)
    en3.place(x=200,y=250)
    bt.place(x=150,y=150)
    top.mainloop()
win.mainloop()

