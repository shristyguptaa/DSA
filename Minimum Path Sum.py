# Minimum Path Sum
grid = [[1,3,1],[1,5,1],[4,2,1]]

for i in range(1,len(grid[0])):
    grid[0][i]+=grid[0][i-1]
for i in range(1,len(grid)):
    grid[i][0]+=grid[i-1][0]
for i in range(1,len(grid)):
    for j in range(1,len(grid[0])):
        grid[i][j]+=min(grid[i][j-1],grid[i-1][j])

print (grid[-1][-1])
