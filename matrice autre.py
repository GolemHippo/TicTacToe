board=[" " for _ in range(9)]
def plateau_jeu():
    print("", board[0],"|", board[1],"|", board[2],"")
    print("---|---|---")
    print("", board[3],"|", board[4],"|", board[5],"")
    print("---|---|---")
    print("", board[6],"|", board[7],"|", board[8],"")
Joueur_actuel='X'
def àqui():
    global Joueur_actuel    
    Joueur_actuel = 'O' if Joueur_actuel == 'X' else 'X'
if all(cell=='X' for cell in  board):
    print('Player X wins')