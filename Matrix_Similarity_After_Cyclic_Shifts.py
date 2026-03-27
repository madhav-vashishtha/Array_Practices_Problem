def areSimilar(mat, k):
    n = len(mat[0])   
    
    k = k % n
    
    for i in range(len(mat)):
        row = mat[i]
        
        if i % 2 == 0:
            shifted = row[k:] + row[:k]
        
        else:
            shifted = row[-k:] + row[:-k]
        
        if shifted != row:
            return False
    
    return True

mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2

print(areSimilar(mat, k))

mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2

print(areSimilar(mat, k))

mat = [[2,2],[2,2]]
k = 3

print(areSimilar(mat, k))

