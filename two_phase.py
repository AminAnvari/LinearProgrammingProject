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


def two_phase(x, r):
    eps = 0.000000000000001
    tmp = x[0][:]

    for i in range(len(x[0])):
        x[0][i] = 0
    x[0][1] = 1
    for i in range(len(x[0]) - 1 - r, len(x[0]) - 1):
        x[0][i] = 1

    for i in range(len(x)):
        if x[i][len(x[i]) - 1] < -eps:
            return 'Impossible!'

    print('phase_1')
    pt(x)
    while True:
        fix_table(x)
        res = lola_table(x)
        pt(x)

        if res != 'Continue!':
            break

    if res != 'Finished!':
        return res

    x[0] = tmp
    for i in range(len(x)):
        for j in range(r):
            x[i].pop(len(x[i]) - 1 - r)
    print('phase_2')
    pt(x)

    while True:
        fix_table(x)
        res = lola_table(x)
        pt(x)
        if res != 'Continue!':
            return res
