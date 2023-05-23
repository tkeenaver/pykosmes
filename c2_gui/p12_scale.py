from tkinter import * 
 
root = Tk()
root.geometry("200x200")
frame = Frame(root)
frame.pack()
 
Scala = Scale(frame, from_=0, to=10)
Scala.pack(padx=5, pady=5)
 
Scala2 = Scale(frame, from_=0, to=10, orient=HORIZONTAL)
Scala2.pack(padx=5, pady=5)
 
root.mainloop()
