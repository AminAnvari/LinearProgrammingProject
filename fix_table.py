def fix_table(x):
    for i in range(len(x)):
        idx = x[i][0] + 1
        pmt = x[i][idx]
        for j in range(1, len(x[i])):
            x[i][j] /= pmt

        for k in range(len(x)):
            if k != i:
                tmp = x[k][idx]
                for j in range(1, len(x[k])):
                    x[k][j] -= tmp * x[i][j]
