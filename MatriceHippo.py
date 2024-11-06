board=[" " for _ in range(9)]

def plateau_jeu():
    print("", board[0],"|", board[1],"|", board[2],"")
    print("---|---|---")
    print("", board[3],"|", board[4],"|", board[5],"")
    print("---|---|---")
    print("", board[6],"|", board[7],"|", board[8],"")
    
def movedujoueur():
    case_jouée=int(input('Où voulez-vous jouez?'))
    if board[case_jouée-1]==' ':
        board[case_jouée-1]=Joueur_actuel
    else:
        print('Vous devez choisir une bonne case!!!')


Joueur_actuel='X'

def changedejoueur():
    global Joueur_actuel    
    Joueur_actuel = 'O' if Joueur_actuel == 'X' else 'X'

def cdts_vic_j1():
    if all(cell=='X' for cell in board[0:3]):
        print('GG WP J1')
    elif all(cell=='X' for cell in board[3:6]):
        print('GG WP J1')
    elif all(cell=='X' for cell in board[6:9]):
        print('GG WP J1')
    elif board[0]==board[4]==board[8]!=' ':
        print('GG WP J1')
    elif board[2]==board[4]==board[6]!=' ':
        print('GG WP J1')

def cdts_vic_j2():
    if all(cell=='O' for cell in board[0:3]):
        print('GG WP J2')
    elif all(cell=='O' for cell in board[3:6]):
        print('GG WP J2')
    elif all(cell=='O' for cell in board[6:9]):
        print('GG WP J2')
    elif 



if all(cell=='X' for cell in board):
    print('Player X wins')

