from tkinter import * 
   
root = Tk()
root.geometry("200x220")
frame = Frame(root)
frame.pack()
 
label = Label(root,text = "A list of Grocery items.")  
label.pack()  
   
listbox = Listbox(root)  
   
listbox.insert(1,"Bread")  
listbox.insert(2, "Milk")  
listbox.insert(3, "Meat")  
listbox.insert(4, "Cheese")
listbox.insert(5, "Vegetables")  
   
listbox.pack()  
root.mainloop()
