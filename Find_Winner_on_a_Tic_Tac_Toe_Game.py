def tictactoe(moves):
    
    board = [["" for _ in range(3)] for _ in range(3)]
    
    for i, move in enumerate(moves):
        r, c = move
        
        if i % 2 == 0:
            board[r][c] = "X"
        else:
            board[r][c] = "O"

    for row in board:
        if row[0] == row[1] == row[2] != "":
            return "A" if row[0] == "X" else "B"
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return "A" if board[0][col] == "X" else "B"
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return "A" if board[0][0] == "X" else "B"
    
    if board[0][2] == board[1][1] == board[2][0] != "":
        return "A" if board[0][2] == "X" else "B"
    
    if len(moves) == 9:
        return "Draw"
    
    return "Pending"


moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(tictactoe(moves))

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(tictactoe(moves))

moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(tictactoe(moves))




