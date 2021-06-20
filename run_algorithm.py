from make_initial_table import make_initial_table
from user_output import user_output
from large_m import large_m
from two_phase import two_phase
from dual_simplex import dual_simplex


def run_algorithm(window, algorithm_number, t, n, m, x):
    if algorithm_number == 1:
        r = make_initial_table(t, n, m, x)
        ans = large_m(x, r)
        user_output(window, ans, t, n, x)
    elif algorithm_number == 2:
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
