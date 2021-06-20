from tkinter import *
from n_input import n_input


def user_input():
    window = Tk()
    window.title("Welcome to Linear Programming app")
    window.geometry('700x400')

    n_input(window)

    window.mainloop()


user_input()
