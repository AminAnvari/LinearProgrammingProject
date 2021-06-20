from tkinter import *
from table_input import table_input


def m_input(window, n):
    lbl = Label(window, text="تعداد قیدهای مسئله")
    lbl.grid(column=0, row=2)

    txt = Entry(window, width=10)
    txt.grid(column=1, row=2)

    def clicked():
        try:
            m = int(txt.get())
            lbl.configure(text="تعداد قیدهای مسئله با موفقیت ثبت شد")
            table_input(window, n, m)

        except Exception as e:
            lbl.configure(text="لطفاً  یک عدد وارد کنید")
            print(e)

    btn = Button(window, text="ثبت کن", command=clicked)
    btn.grid(column=3, row=2)
