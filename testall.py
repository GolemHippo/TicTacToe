board=[" " for _ in range(9)]
board[6]='X'
board[7]='X'
board[8]='X'
if all(cell=='X' for cell in board[5:9]):
    print('yessai')
print(board)