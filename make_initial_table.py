def make_initial_table(t, n, m, x):
    s, r = 0, 0
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
            x[i].insert(0, n + 1 + s + cnt_r)
            cnt_s += 1
            cnt_r += 1
        else:
            x[i][n + 1 + s + cnt_r] = 1
            x[i].insert(0, n + 1 + s + cnt_r)
            cnt_r += 1

    for i in range(len(x)):
        x[i].pop(len(x[i]) - 2)

    if t == 'MIN':
        for i in range(2, len(x[0])):
            x[0][i] *= -1

    return r
