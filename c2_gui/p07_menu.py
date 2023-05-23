from tkinter import *
 
def save():
    #Code to be written
    pass
 
def load():
    #Code to be written
    pass   
 
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
 
mainmenu = Menu(frame)
mainmenu.add_command(label = "Save", command= save)  
mainmenu.add_command(label = "Load", command= load)
mainmenu.add_command(label = "Exit", command= root.destroy)
 
root.config(menu = mainmenu)
 
root.mainloop()