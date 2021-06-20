from tkinter.ttk import Combobox
from tkinter import *
from n_input import n_input


def type_input(window):
    lbl = Label(window, text="نوع حل مسئله را مشخص کنید")
    lbl.grid(column=0, row=1)

    combo = Combobox(window)
    combo['values'] = ('MIN', 'MAX')
    combo.grid(column=1, row=1)

    def clicked():
        try:
            t = combo.get()
            lbl.configure(text="نوع حل مسئله با موفقیت ثبت شد")
            n_input(window, t)

        except Exception as e:
            lbl.configure(text="لطفاٌ از داخل جعبه انتخاب کنید!")
            print(e)

    btn = Button(window, text="ثبت کن", command=clicked)
    btn.grid(column=3, row=1)
