from tkinter import*
from tkinter import ttk, messagebox

class rom:
    def __init__(self,win):
        self.win=win
        self.title("Restaurant App")
        self.menu_items={
            "FRENCH FRIES":2,
            "PIZZA":3,
            "BURGER":2.5,
            "TACO":5,
            "JUICE":4
        }

        self.exchange_rate=82
        self.setup_background(win)
        frame=ttk.Frame(win)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,
                  text="Restaurant App"
                  font("Arial",20,"bold")).grid(
                      row=0,
                      columnspan=3,
                      padx=10,
                      pady=10
                  )
        self.menu_label={}
        self.menu_quantities={}

        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_quantities[item]=quantity_entry

        self.currency_var=tk.StringVar()
        ttk.Label(frame,text="Currency:",
                  font=("Arial",12)).grid(row=len(self.menu_items)+1,
                                          column=0
                                          padx=10
                                          pady=5)
        
        currency_dropdown=ttk.ComboBox(frame,
                                       textvariable=self.currency_var,
                                       state="readonly",
                                       width=18,
                                       values=("USD","INR"))
