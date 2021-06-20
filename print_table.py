from tkinter import *


def print_table(window, row, x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            lbl = Label(window, text=str(x[i][j]))
            lbl.grid(column=j, row=i+row)
