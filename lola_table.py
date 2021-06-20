def lola_table(x):
    eps = 0.000000000000001
    c_idx = -1
    for i in range(1, len(x[0]) - 1):
        if c_idx == -1 or x[0][i] < x[0][c_idx]:
            c_idx = i

    if c_idx == -1 or x[0][c_idx] >= -eps:
        return 'Finished!'

    r_idx = -1
    for i in range(1, len(x)):
        if x[i][c_idx] > eps and \
                (r_idx == -1 or x[i][len(x[i]) - 1] / x[i][c_idx] < x[r_idx][len(x[r_idx]) - 1] / x[r_idx][c_idx]):
            r_idx = i

    if r_idx == -1:
        return 'Infinity!'

    x[r_idx][0] = c_idx - 1
    return 'Continue!'
