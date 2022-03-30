# Set Matrix Zeroes
matrix = [[1,1,1],[1,0,1],[1,1,1]]

tmp = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            for k in range(len(matrix[0])):
                tmp[i][k] = 0
            for k in range(len(matrix)):
                tmp[k][j] = 0
matrix[:] = tmp[:]
