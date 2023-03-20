# import tkinter module
# create window object
# define function(s)
# instantiate stringVar object
# create and position labels 
# create and position entry fields
# create and position command button(s)
# invoke mainloop method

from tkinter import *
from tkinter import messagebox

win = Tk()
win.configure(bg="cyan")
win.geometry("500x400+100+100")
win.title("POS App")

def sell():
    # a = str(entryProductCode.get())
    try:
        b = int(entryQuantity.get())
        c = int(entryPrice.get())
        d = b*c
    except: 
        messagebox.showwarning("input","enter values")  
        clear()
        entryProductCode.focus() #the cursor will move to the product code textbox
    else:
        cost =str(d)
        var1.set(cost)
        messagebox.showinfo("info", "thank you")



def clear():
    entryProductCode.delete(0,END)
    entryQuantity.delete(0,END)
    entryPrice.delete(0,END)
    entryCost.delete(0,END)

    messagebox.showinfo("CLEARANCE","CLEARED")


var1 = StringVar()

lblProductCode = Label(win,text="Product Code", bg="cyan")
lblQuantity = Label(win,text="Quantity", bg="cyan")
lblPrice = Label(win,text="Product Price", bg="cyan")
lblCost = Label(win,text="Product Cost", bg="cyan")

lblProductCode.grid(row=0,sticky=W)
lblQuantity.grid(row=1,sticky=W)
lblPrice.grid(row=2,sticky=W)
lblCost.grid(row=3,sticky=W)

entryProductCode = Entry(win)
entryQuantity = Entry(win)
entryPrice = Entry(win)
entryCost = Entry(win,textvariable=var1)

entryProductCode.grid(row=0,column=2)
entryQuantity.grid(row=1,column=2)
entryPrice.grid(row=2,column=2)
entryCost.grid(row=3,column=2)

btnSell = Button(win,text="sell",bg="blue",command=sell)
btnClear = Button(win,text="clear",bg="blue",command=clear)

btnSell.grid(row=4,column=0)
btnClear.grid(row=4,column=3)

win.mainloop()

