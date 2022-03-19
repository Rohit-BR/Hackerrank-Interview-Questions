def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s


A = [[112,56,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]
print(flippingMatrix(A))
