import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x200")

frame1 = tk.Frame(root)
frame1.pack(fill=tk.BOTH, expand=True)

label1 = tk.Label(frame1, text="Pack")
label1.pack()

frame2 = tk.Frame(root)
frame2.pack(fill=tk.BOTH, expand=True)

label2 = tk.Label(frame2, text="Grid")
label2.grid(row=0, column=0)

label3 = tk.Label(frame2, text="Place")
label3.place(x=50, y=50)  # 좌표!!!

root.mainloop()