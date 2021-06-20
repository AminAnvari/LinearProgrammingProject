def dual_simplex(t, n, m, x):
    for i in range(1, m + 1):
        if x[i][n] == '=':
            tmp = x[i][:]
            x[i][n] = '<='
            tmp[n] = '>='
            x.append(tmp)
            m += 1

    # for i in range(1, m + 1):
    #     if x[i][n] == '>=' and t == 'MAX':
    #         for j in range(0, n):
    #             x[i][j] *= -1
    #         x[i][n] = '<='
    #         x[i][n + 1] *= -1
    #     if x[i][n] == '<=' and t == 'MIN':
    #         for j in range(0, n):
    #             x[i][j] *= -1
    #         x[i][n] = '>='
    #         x[i][n + 1] *= -1

    func = []
    for i in range(1, len(x)):
        func.append(x[i][len(x[i]) - 1])

    y = [func]
    for i in range(n):
        row = []
        for j in range(1, m + 1):
            row.append(x[j][i])
        y.append(row)

        if t == 'MAX':
            y.append('<=')
        else:
            y.append('>=')

        y.append(x[0][i])

    x = y
    return n, m
