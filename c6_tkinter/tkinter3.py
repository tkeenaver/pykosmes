import tkinter as tk

root = tk.Tk()

def calculate():
    result = eval(entry.get())
    label_result.config(text=f"Result: {result}")

entry = tk.Entry(root)
entry.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

tk.mainloop()