def rotate(matrix):
    n = len(matrix)
    new = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new[j][n-1-i] = matrix[i][j]
    
    return new

def findRotation(mat, target):
    for _ in range(4):
        if mat == target:
            return True
        mat = rotate(mat) 
    
    return False

mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]

print(findRotation(mat, target))

mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]

print(findRotation(mat, target))

mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]

print(findRotation(mat, target))

