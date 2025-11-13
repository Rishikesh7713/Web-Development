from tkinter import*
from PIL import Image, ImageTk
import random
win=Tk()
win.geometry=("700x600")
win.title("Rock Paper Scissor App")

upload1=Image.open("money.jpg")
upload1=upload1.resize((300,300))
rock=ImageTk.PhotoImage(upload1)
upload2=Image.open("money.jpg")
upload1=upload2.resize((300,300))
paper=ImageTk.PhotoImage(upload2)
upload3=Image.open("money.jpg")
upload3=upload3.resize((300,300))
scissor=ImageTk.PhotoImage(upload3)
lbl1=Label(win,text="Hey There! This is a Rock Paper Scissor App",bg="light blue")
lbl1.place(relx=0.5,y=350)
rps={rock,paper,scissor}
input=""
def rocks():
    input="rock"
def papers():
    input="paper"
def scissors():
    input="scissor"

def dis():
    com=random.choices(rps)
    pl=input
    if pl == com:
            txt.insert("It  is a Tie")
    elif (pl == "Rock" and com == "Scissors") or \
             (pl == "Paper" and com == "Rock") or \
             (pl == "Scissors" and com == "Paper"):
        txt.insert("Player wins!")
            
    else:
          txt.insert("Computer Wins!") 
btn_rock=Button(command=rocks,text="Rock")
btn_paper=Button(command=papers,text="Paper")
btn_scissor=Button(command=scissors,text="Scissor")
btn=Button(command=dis)
txt=Text()
btn_rock.pack()
btn_paper.pack()
btn_scissor.pack()
btn.pack()
txt.pack()
win.mainloop()