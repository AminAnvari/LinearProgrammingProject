from make_initial_table import make_initial_table
from user_output import user_output
from large_m import large_m
from two_phase import two_phase
from dual_simplex import dual_simplex


def run_algorithm(window, algorithm_number, n, m, x):
    r = make_initial_table(n, m, x)
    if algorithm_number == 1:
        ans = large_m(x, r)
        user_output(window, ans, x)
    elif algorithm_number == 2:
        ans = two_phase(x, r)
    elif algorithm_number == 3:
        dual_simplex()
    else:
        print('NO item is selected!')
