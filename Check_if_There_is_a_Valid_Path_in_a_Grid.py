from collections import deque

def hasValidPath(grid):
    m, n = len(grid), len(grid[0])
    
    dirs = {
        1: [(0, -1), (0, 1)],    
        2: [(-1, 0), (1, 0)],    
        3: [(0, -1), (1, 0)],     
        4: [(0, 1), (1, 0)],   
        5: [(0, -1), (-1, 0)],  
        6: [(0, 1), (-1, 0)]   
    }
    
    def is_connected(x, y, nx, ny):
        dx = nx - x
        dy = ny - y
        return (-dx, -dy) in dirs[grid[nx][ny]]
    
    visited = set()
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (m-1, n-1):
            return True
        
        visited.add((x, y))
        
        for dx, dy in dirs[grid[x][y]]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if is_connected(x, y, nx, ny):
                    queue.append((nx, ny))
    
    return False

grid = [[2,4,3],[6,5,2]]
print(hasValidPath(grid))  

grid = [[1,2,1],[1,2,1]]
print(hasValidPath(grid))  

grid = [[1,1,2]]
print(hasValidPath(grid))  


