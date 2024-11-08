import random 
signe='O'
board=[1,2,3,4,5,' ']
def ia(board,signe):
    cases_vide =  [i for i in range(len(board)) 
                   if board[i] is board[i] == " "] 
    print(cases_vide)

ia(board,signe)