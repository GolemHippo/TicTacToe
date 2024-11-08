import random 

def ia(board,signe):
    cases_vide =  [i for i in range(len(board)) 
                   if board[i] is board[i] == " "] 
    if cases_vide:
            choix = random(cases_vide)
            board[choix] = signe
            if signe:
                print("O")
            else:
                print("il n'y a plus de case a jouer")

