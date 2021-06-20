from tkinter import *
from run_algorithm import run_algorithm


def algorithm_input(window, n, m, x):
    selected = IntVar()
    rad1 = Radiobutton(window, text='روش M-بزرگ', value=1, variable=selected)
    rad1.grid(column=0, row=20)

    rad2 = Radiobutton(window, text='روش دو فازی', value=2, variable=selected)
    rad2.grid(column=1, row=20)

    rad3 = Radiobutton(window, text='روش دوگان', value=3, variable=selected)
    rad3.grid(column=2, row=20)

    def clicked():
        algorithm_number = selected.get()
        run_algorithm(window, algorithm_number, n, m, x)

    solve_btn = Button(window, text="حل کن", command=clicked)
    solve_btn.grid(column=3, row=20)
