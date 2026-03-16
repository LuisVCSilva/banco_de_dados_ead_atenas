rows, cols = 2, 3
mat = [[i + j*cols + 1 for i in range(cols)] for j in range(rows)]

for row in mat:
    print(row)
