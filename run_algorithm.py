from make_initial_table import make_initial_table
from user_output import user_output
from large_m import large_m
from two_phase import two_phase
from dual_simplex import dual_simplex


def b_fix(x):
    for i in range(1, len(x)):
        if x[i][len(x[i]) - 1] < 0:
            for j in range(len(x[i]) - 2):
                x[i][j] *= -1
            if x[i][len(x[i]) - 2] == '<=':
                x[i][len(x[i]) - 2] = '>='
            elif x[i][len(x[i]) - 2] == '>=':
                x[i][len(x[i]) - 2] = '<='
            x[i][len(x[i]) - 1] *= -1


def run_algorithm(window, algorithm_number, t, n, m, x):
    if algorithm_number == 1:
        b_fix(x)
        r = make_initial_table(t, n, m, x)
        ans = large_m(x, r)
        user_output(window, ans, t, n, x)
    elif algorithm_number == 2:
        b_fix(x)
        r = make_initial_table(t, n, m, x)
        ans = two_phase(x, r)
        user_output(window, ans, t, n, x)
    elif algorithm_number == 3:
        n, m = dual_simplex(t, n, m, x)
        r = make_initial_table(t, n, m, x)
        ans = large_m(x, r)
        user_output(window, ans, t, n, x)
    else:
        print('NO item is selected!')
