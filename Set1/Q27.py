def matrix_spiral_print(M):
    R = len(M[0])
    C = len(M)

    k = 0
    l = 0

    while(k < R and l < C):

        for i in range(l, C):
            print M[k][i]
        k+=1

        for i in range(k,R):
            print M[i][C-1]

        C -=1

        if (k < R):
            for i in range(C-1, (l-1), -1):
                print M[R-1][i]

            R -= 1

        if (l < C):
            for i in range(R-1, k-1, -1):
                print M[i][l]

            l += 1

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12