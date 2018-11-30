import numpy as np

def changem(mat, n1):
    for x in range(0, n1):
        for y in range(0, n1):
            lst = neighbors(x, y)
            if mat[x][y] == 0:
                if len(lst)/2 < sum([mat[lst[i][0]][lst[i][1]] for i in range(0, len(lst))]):
                    mat[x][y] = 1
            else:
                if len(lst)/2 > sum([mat[lst[i][0]][lst[i][1]] for i in range(0, len(lst))]):
                    mat[x][y] = 0

n  = 5

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= n and
                                   -1 < y <= n and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 < n) and
                                   (0 <= y2 < n))]

matrix = np.random.choice([0, 1], size=(n,n))

print(matrix)

changem(matrix, n)

print(matrix)
