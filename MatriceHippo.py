board=[" " for _ in range(9)]

Joueur_actuel='X'

result='ingame'

def plateau_jeu():
    print("", board[0],"|", board[1],"|", board[2],"")
    print("---|---|---")
    print("", board[3],"|", board[4],"|", board[5],"")
    print("---|---|---")
    print("", board[6],"|", board[7],"|", board[8],"")



def changedejoueur():
    global Joueur_actuel    
    Joueur_actuel = 'O' if Joueur_actuel == 'X' else 'X'

def movedujoueur():
    case_jouée=int(input('Où voulez-vous jouez?'))
    if 1<=case_jouée<=9:
        if board[case_jouée-1]==' ':
            board[case_jouée-1]=Joueur_actuel
            changedejoueur()
        else:
            print('Vous devez choisir une bonne case!!!')
    else:
        print(' Vous devez choisir une case comprise entre 1 et 9 !!!')



def cdts_vic_j1():
    global result
    if all(cell=='X' for cell in board[0:3]):
        result=1
        print('GG WP J1')
    elif all(cell=='X' for cell in board[3:6]):
        result=1
        print('GG WP J1')
    elif all(cell=='X' for cell in board[6:9]):
        result=1
        print('GG WP J1')
    elif board[0]==board[4]==board[8]=='X':
        result=1
        print('GG WP J1')
    elif board[2]==board[4]==board[6]=='X':
        result=1
        print('GG WP J1')

def cdts_vic_j2():
    global result
    if all(cell=='O' for cell in board[0:3]):
        result=2
        print('GG WP J2')
    elif all(cell=='O' for cell in board[3:6]):
        result=2
        print('GG WP J2')
    elif all(cell=='O' for cell in board[6:9]):
        result=2
        print('GG WP J2')
    elif board[0]==board[4]==board[8]=='O':
        result=2
        print('GG WP J2')
    elif board[2]==board[4]==board[6]=='O':
        result=2
        print('GG WP J2')
    

def draw():
    global result
    if all(cell!=' ' for cell in board):
        result=0
        print('Belle partie,\nMatch nul')

while True:
    if result=='ingame':    
        plateau_jeu()
        movedujoueur()
        cdts_vic_j1()
        cdts_vic_j2()
        draw()
        print(result)
    elif result=='1':
        print('ggj1')
    elif result=='2':
        print('ggj2')
    elif result=='0':
        print('ggdraw')