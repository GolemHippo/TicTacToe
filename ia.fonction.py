import random 
signe = "O"
def ia(board,signe):
    cases_vide =  [i for i in range(len(board)) 
                   if board[i] is board[i] == " "] 
    choix = random(cases_vide)
    board[choix] = signe

