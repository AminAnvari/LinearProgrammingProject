from tkinter.ttk import Combobox
from tkinter import *
from algorithm_input import algorithm_input


def table_input(window, n, m):
    x = []
    table_boxes = []
    function = []
    for i in range(n):
        lbl = Label(window, text='y' + str(i + 1))
        lbl.grid(column=2*i+0, row=3)

        txt = Entry(window, width=5)
        txt.grid(column=2*i+1, row=3)

        function.append(txt)

    table_boxes.append(function)

    for i in range(m):
        row_boxes = []
        for j in range(n):
            lbl = Label(window, text='x' + str(i + 1) + ',' + str(j + 1))
            lbl.grid(column=2*j+0, row=4+i)

            txt = Entry(window, width=5)
            txt.grid(column=2*j+1, row=4+i)

            row_boxes.append(txt)

        combo = Combobox(window)
        combo['values'] = ('=', '<=', '>=')
        combo.grid(column=2*n, row=4 + i)

        lbl = Label(window, text='b' + str(i + 1))
        lbl.grid(column=2*n+1, row=4 + i)

        txt = Entry(window, width=5)
        txt.grid(column=2*n+2, row=4 + i)

        row_boxes.append(combo)
        row_boxes.append(txt)
        table_boxes.append(row_boxes)

    def clicked():
        try:
            x_func = []
            for c in range(n):
                x_func.append(int(table_boxes[0][c].get()))
            x.append(x_func)

            for rr in range(1, m + 1):
                x_row = []
                for c in range(n):
                    x_row.append(int(table_boxes[rr][c].get()))

                x_row.append(table_boxes[rr][n].get())
                assert(x_row[n] in ['=', '<=', '>='])
                x_row.append(int(table_boxes[rr][n + 1].get()))

                x.append(x_row)

            algorithm_input(window, n, m, x)
        except Exception as e:
            lbl.configure(text="لطفاً درست وارد کنید!")
            print(e)

    btn = Button(window, text="ثبت کن", command=clicked)
    btn.grid(column=3, row=4+m)
