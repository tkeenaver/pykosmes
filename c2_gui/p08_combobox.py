from tkinter import *
from tkinter import ttk
 
root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
 
vlist = ["Option1", "Option2", "Option3",
          "Option4", "Option5"]
 
Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Pick an Option")
Combo.pack(padx = 5, pady = 5)
 
root.mainloop()