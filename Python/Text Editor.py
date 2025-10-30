from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename
win=Tk()
win.geometry("700x600")
win.title("Text Editor App")
win.rowconfigure(0,minsize=800,weight=1)
win.columnconfigure(1,minsize=800,weight=1)

def openfile():
    filepath=askopenfilename(
        filetypes=[("Text files","*.txt"),("All files","*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text=input_file.read()
        text_edit.insert(END,text)
        input_file.close()
    win.title("File - {filepath}")

def savefile():
    filepath=asksaveasfilename(
        defaultextension="txt",filetypes=[("Text files","*.txt"),("All files","*.*")]
    )
    if not filepath:
        return
    
    with open(filepath,"w") as output_file:
        text=text_edit.get(1.0,END)
        output_file.write(text)
    win.title("File - {filepath}")

text_edit=Text(win)
fr_but=Frame(win,relief=RAISED,bd=2)
btn1=Button(fr_but,text="Open",command=openfile)
btn2=Button(fr_but,text="Save As",command=savefile)
btn1.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn2.grid(row=1,column=0,sticky="ew",padx=5)
fr_but.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsew")

win.mainloop()