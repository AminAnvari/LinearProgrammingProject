from tkinter import *
from print_text import print_text


def print_table(window, row, t, n, x):
    eps = 0.00001
    ans = [0] * n
    for i in range(1, len(x)):
        if x[i][0] <= n:
            ans[x[i][0] - 1] = x[i][len(x[i]) - 1]

    z = x[0][len(x[0]) - 1]
    if t == 'MIN':
        z *= -1

    for val in ans:
        if val < 0.0:
            print_text(window, row, 'Impossible!')

    lbl = Label(window, text='Z: ' + str(format(z, '.3f')))
    lbl.grid(column=0, row=row)

    for i in range(n):
        val = ans[i] + eps
        lbl = Label(window, text='x' + str(i + 1) + '= ' + str(format(val, '.3f')))
        lbl.grid(column=1+i, row=row)
