from tkinter import *
from m_input import m_input


def n_input(window):
    lbl = Label(window, text="تعداد متغیرهای تصمیم")
    lbl.grid(column=0, row=1)

    txt = Entry(window, width=10)
    txt.grid(column=1, row=1)

    def clicked():
        try:
            n = int(txt.get())
            lbl.configure(text="تعداد متغیرهای تصمیم با موفقیت ثبت شد")
            m_input(window, n)

        except Exception as e:
            lbl.configure(text="لطفاً  یک عدد وارد کنید")
            print(e)

    btn = Button(window, text="ثبت کن", command=clicked)
    btn.grid(column=3, row=1)
