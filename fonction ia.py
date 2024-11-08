joueur1='X'
signe='O'
board=[" " for _ in range(9)]
import random

print (board)

def ia(board,signe):
    
    while True:
        global number_ai
        number_ia=random.randint(0,8)
        move_ia=board[number_ia]
        if move_ia==' ':
            board[number_ia]=signe
            break



ia(board,signe)

print(board)
