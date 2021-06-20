from tkinter import *
from type_input import type_input


def user_input():
    window = Tk()
    window.title("Welcome to Linear Programming app")
    window.geometry('700x400')

    type_input(window)

    window.mainloop()


user_input()
