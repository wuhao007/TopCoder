class MutaliskEasy:
    def minimalAttacks(self, x):
        I, J, K = 60, 60, 60
        if len(x) == 1:
            I, J, K = x[0], 1
        elif len(x) == 2:
            I, J, K = x[0], x[1], 1
        else:
            I, J, K = x[0], x[1], x[2]
        matrix = [[[60 for k in range(K + 1)] for j in range(J + 1)] for i in range(I + 1)] 
        for i in range(I + 1):
            for j in range(J + 1):
                for k in range(K + 1):
                    f, s, t = sorted([i, j, k])
                    if i == j == k == 0:
                        matrix[i][j][k] = 0
                    elif f <= 1 and s <= 3 and t <= 9:
                        matrix[i][j][k] = 1
                    else:
                        f, s, t = max(i - 1, 0), max(j - 3, 0), max(k - 9, 0)
                        matrix[i][j][k] = matrix[f][s][k] + 1
                        f, s, t = max(i - 1, 0), max(j - 9, 0), max(k - 3, 0)
                        matrix[i][j][k] = min(matrix[i][j][k], matrix[f][s][k] + 1)
                        f, s, t = max(i - 3, 0), max(j - 1, 0), max(k - 9, 0)
                        matrix[i][j][k] = min(matrix[i][j][k], matrix[f][s][k] + 1)
                        f, s, t = max(i - 3, 0), max(j - 9, 0), max(k - 1, 0)
                        matrix[i][j][k] = min(matrix[i][j][k], matrix[f][s][k] + 1)
                        f, s, t = max(i - 9, 0), max(j - 1, 0), max(k - 3, 0)
                        matrix[i][j][k] = min(matrix[i][j][k], matrix[f][s][k] + 1)
                        f, s, t = max(i - 9, 0), max(j - 3, 0), max(k - 1, 0)
                        matrix[i][j][k] = min(matrix[i][j][k], matrix[f][s][k] + 1)
        return matrix[I][J][K]
mutaliskEasy = MutaliskEasy()
print mutaliskEasy.minimalAttacks((12, 10, 4))
print mutaliskEasy.minimalAttacks((55, 60, 53))
