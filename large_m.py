from fix_table import fix_table
from lola_table import lola_table


# Just For DEBUG
def pt(t):
    print("printing")
    for i in range(len(t)):
        for j in range(len(t[i])):
            if int(t[i][j]) >= 0:
                print('+' + str(int(t[i][j])), end=' ')
            else:
                print(int(t[i][j]), end=' ')
        print()
    print()


def large_m(x, r):
    eps = 0.000000000000001
    large_value = 10000
    for i in range(len(x[0]) - r - 1, len(x[0]) - 1):
        x[0][i] = large_value

    for i in range(len(x)):
        if x[i][len(x[i]) - 1] < -eps:
            return 'Impossible!'

    while True:
        pt(x)
        fix_table(x)
        res = lola_table(x)

        if res != 'Continue!':
            return res
