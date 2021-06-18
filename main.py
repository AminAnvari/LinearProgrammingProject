from tkinter.ttk import Combobox
from tkinter import *

window = Tk()
n, m, r, s = 0, 0, 0, 0
x = []
t = []


def n_input():
    global window
    lbl = Label(window, text="تعداد متغیرهای تصمیم")
    lbl.grid(column=0, row=1)

    txt = Entry(window, width=10)
    txt.grid(column=1, row=1)

    def clicked():
        try:
            global n
            n = int(txt.get())
            lbl.configure(text="تعداد متغیرهای تصمیم با موفقیت ثبت شد")
            print('n: ' + str(n))
            m_input()

        except Exception as e:
            lbl.configure(text="لطفاً  یک عدد وارد کنید")
            print(e)

    btn = Button(window, text="ثبت کن", command=clicked)
    btn.grid(column=3, row=1)


def m_input():
    global window
    lbl = Label(window, text="تعداد قیدهای مسئله")
    lbl.grid(column=0, row=2)

    txt = Entry(window, width=10)
    txt.grid(column=1, row=2)

    def clicked():
        try:
            global m
            m = int(txt.get())
            print('m: ' + str(m))
            lbl.configure(text="تعداد قیدهای مسئله با موفقیت ثبت شد")
            table_input()

        except Exception as e:
            lbl.configure(text="لطفاً  یک عدد وارد کنید")
            print(e)

    btn = Button(window, text="ثبت کن", command=clicked)
    btn.grid(column=3, row=2)


def table_input():
    global n, m, x, window

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

            print('x: ' + str(x))
            algorithm_input()
        except Exception as e:
            lbl.configure(text="لطفاً درست وارد کنید!")
            print(e)

    btn = Button(window, text="ثبت کن", command=clicked)
    btn.grid(column=3, row=4+m)


def algorithm_input():
    global window
    selected = IntVar()
    rad1 = Radiobutton(window, text='روش M-بزرگ', value=1, variable=selected)
    rad1.grid(column=0, row=20)

    rad2 = Radiobutton(window, text='روش دو فازی', value=2, variable=selected)
    rad2.grid(column=1, row=20)

    rad3 = Radiobutton(window, text='روش دوگان', value=3, variable=selected)
    rad3.grid(column=2, row=20)

    def clicked():
        algorithm_number = selected.get()
        print('algorithm_number: ' + str(algorithm_number))
        run_algorithm(algorithm_number)

    solve_btn = Button(window, text="حل کن", command=clicked)
    solve_btn.grid(column=3, row=20)


def user_input():
    global window
    window.title("Welcome to Linear Programming app")
    window.geometry('700x400')

    n_input()

    window.mainloop()


def pt():
    print("printing")
    global t
    for i in range(len(t)):
        for j in range(len(t[i])):
            if int(t[i][j]) >= 0:
                print('+' + str(int(t[i][j])), end=' ')
            else:
                print(int(t[i][j]), end=' ')
        print()
    print()


def fix_table():
    global t
    for i in range(len(t)):
        idx = t[i][0] + 1
        pmt = t[i][idx]
        for j in range(1, len(t[i])):
            t[i][j] /= pmt

        for k in range(len(t)):
            if k != i:
                tmp = t[k][idx]
                for j in range(1, len(t[k])):
                    t[k][j] -= tmp * t[i][j]


def lola_table():
    global t
    c_idx = -1
    for i in range(1, len(t[0])):
        if c_idx == -1 or t[0][i] < t[0][c_idx]:
            c_idx = i

    if c_idx == -1 or t[0][c_idx] >= -0.000001:
        return 'Finished!'

    r_idx = -1
    for i in range(1, len(t)):
        if t[i][c_idx] > 0 and \
                (r_idx == -1 or t[i][len(t[i]) - 1] / t[i][c_idx] > t[r_idx][len(t[r_idx]) - 1] / t[r_idx][c_idx]):
            r_idx = i

    if r_idx == -1:
        return 'Finished!'

    t[r_idx][0] = c_idx - 1
    return 'Continue!'


def make_initial_table():
    global t, n, m, x, r, s
    for i in range(1, m + 1):
        if x[i][n] == '<=':
            s += 1
        elif x[i][n] == '>=':
            s += 1
            r += 1
        else:
            r += 1

    for i in range(m + 1):
        x[i].insert(0, 0)
        for j in range(r + s):
            x[i].insert(n + 1, 0)

    x[0] += ['=']
    x[0].append(0)
    for j in range(len(x[0]) - 2):
        x[0][j] *= -1
    x[0][0] = 1

    x[0].insert(0, 0)
    cnt_s, cnt_r = 0, 0
    for i in range(1, m + 1):
        if x[i][n + 1 + r + s] == '<=':
            x[i][n + 1 + cnt_s] = 1
            x[i].insert(0, n + 1 + cnt_s)
            cnt_s += 1
        elif x[i][n + 1 + r + s] == '>=':
            x[i][n + 1 + cnt_s] = -1
            x[i][n + 1 + s + cnt_r] = 1
            x[i].insert(0, n + 1 + cnt_s)
            cnt_s += 1
            cnt_r += 1
        else:
            x[i][n + 1 + s + cnt_r] = 1
            x[i].insert(0, n + 1 + s + cnt_r)
            cnt_r += 1

    for i in range(len(x)):
        x[i].pop(len(x[i]) - 2)

    t = x


def large_m():
    pt()
    global t, r
    large_value = 10000
    for i in range(len(t[0]) - r, len(t[0])):
        t[0][i] = large_value

    while True:
        fix_table()
        res = lola_table()

        if res == 'Finished!':
            break


def two_phase():
    pass


def dual_simplex():
    pass


def run_algorithm(algorithm_number):
    make_initial_table()
    if algorithm_number == 1:
        large_m()
        user_output()
    elif algorithm_number == 2:
        two_phase()
    elif algorithm_number == 3:
        dual_simplex()
    else:
        print('NO item is selected!')


def print_table(row):
    global window
    for i in range(len(t)):
        for j in range(len(t[i])):
            lbl = Label(window, text=str(t[i][j]))
            lbl.grid(column=j, row=i+row)


def user_output():
    print_table(100)


user_input()
