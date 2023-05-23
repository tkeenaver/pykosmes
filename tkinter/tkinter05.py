import tkinter as tk
from tkinter import ttk

def display_options(widget):
    config = widget.configure()
    for key, value in config.items():
        print(f'{key:15s}\t{value}')

widget = ttk.Label(None)
display_options(widget)
