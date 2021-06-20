from tkinter import *


def print_table(window, row, t, n, x):
    var = []
    for i in range(1, len(x)):
        if x[i][0] <= n:
            var.append(x[i][0] - 1)

    print(var)

    z = x[0][len(x[0]) - 1]
    if t == 'MIN':
        z *= -1

    lbl = Label(window, text='Z: ' + str(z))
    lbl.grid(column=0, row=row)

    for i in range(n):
        if i in var:
            lbl = Label(window, text='x' + str(i + 1) + '= ' + str(x[1 + i][len(x[1 + i]) - 1]))
            lbl.grid(column=1+i, row=row)
