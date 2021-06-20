from tkinter import *


def print_text(window, row, s):
    lbl = Label(window, text=s)
    lbl.grid(column=0, row=row)
