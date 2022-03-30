# Set Matrix Zeroes
matrix = [[1,1,1],[1,0,1],[1,1,1]]

# Solution 1
tmp = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            for k in range(len(matrix[0])):
                tmp[i][k] = 0
            for k in range(len(matrix)):
                tmp[k][j] = 0
matrix[:] = tmp[:]

# Solution 2
row = [1]*len(matrix)
col = [1]*len(matrix[0])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            row[i] = 0
            col[j] = 0
for r in range(len(row)):
    if row[r] == 0:
        for i in range(len(matrix[0])):
            matrix[r][i] = 0
for j in range(len(col)):
    if col[j] == 0:
        for i in range(len(matrix)):
            matrix[i][j] = 0

# Solution 3
rows = set()
cols = set()
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j]==0:
            rows.add(i)
            cols.add(j)
for i in rows:
    for j in range(len(A[0])):
        A[i][j] = 0
for j in cols:
    for i in range(len(A)):
        A[i][j] = 0
return A
