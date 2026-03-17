def largestSubmatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] += matrix[i-1][j]
    
    max_area = 0
    
    for row in matrix:
        row.sort(reverse=True) 
        
        for j in range(n):
            area = row[j] * (j + 1)
            max_area = max(max_area, area)
    
    return max_area

matrix = [[0,0,1],
          [1,1,1],
          [1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,0,1,0,1]]

print(largestSubmatrix(matrix))

matrix = [[1,1,0],
          [1,0,1]]

print(largestSubmatrix(matrix))
