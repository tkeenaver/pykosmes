import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x200")

# Label 위젯
label = tk.Label(root, text="This is a label")
label.pack()

# Button 위젯
def on_button_click():
    print("Button clicked")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Entry 위젯
entry = tk.Entry(root)
entry.pack()

# Text 위젯
text = tk.Text(root, height=5, width=30)
text.pack()

root.mainloop()