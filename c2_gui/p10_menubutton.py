from tkinter import *
 
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
 
MenuBttn = Menubutton(frame, text = "Favourite food", relief = RAISED)
 
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
 
Menu1 = Menu(MenuBttn, tearoff = 0)
 
Menu1.add_checkbutton(label = "Pizza", variable = Var1)
Menu1.add_checkbutton(label = "Cheese Burger", variable = Var2)
Menu1.add_checkbutton(label = "Salad", variable = Var3)
 
MenuBttn["menu"] = Menu1
 
MenuBttn.pack()
root.mainloop()
