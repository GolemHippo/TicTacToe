board=[" " for _ in range(9)] #Crées une liste, avec une boucle, composée de 9 variables vides : ' ' pour les 9 cases de la matrice.

Joueur_actuel='X' #Définis le premier joueur comme le joueur 'X'.

result='ingame' #Définis l'état de la partie comme en cours.


def plateau_jeu(): #Fonction affichant la matrice du jeu et chaque case grâce à la liste board. 
    print("", board[0],"|", board[1],"|", board[2],"")
    print("---|---|---")
    print("", board[3],"|", board[4],"|", board[5],"")
    print("---|---|---")
    print("", board[6],"|", board[7],"|", board[8],"")


def movedujoueur():#Places un 'X' ou un 'O' en alternance à chaque tour.
    case_jouée=int(input('Où voulez-vous jouez?')) #Demandes au joueur sur quelle case il veut jouer.
    if 1<=case_jouée<=9:
        if board[case_jouée-1]==' ': #La liste commence à l'indexe 0 donc n-1 par rapport à la matrice. #Vérifie que la case choisie est bien vide.
            board[case_jouée-1]=Joueur_actuel#Remplaces la variable correspondant à la case choisie par 'X' ou 'O'.
            changedejoueur() #Appelles la fonction "changedejoueur" pour changer de joueur après chaque coup.
        else: #Si la case n'est pas vide alors elle a déjà été jouée.
            print('Vous devez choisir une bonne case!!!')
    else: #Si la case choisie n'est pas entre 1 et 9 alors elle n'est pas valide.
        print(' Vous devez choisir une case comprise entre 1 et 9 !!!')


def changedejoueur(): #Changes de joueur si l'autre joueur vient de jouer.
    global Joueur_actuel #Permet à la fonction de modifier à l'échelle globale la variable 'Joueur_actuel'.
    Joueur_actuel = 'O' if Joueur_actuel == 'X' else 'X' #Si le joueur actuel est 'X' alors le prochain coup sera pour 'O'.


def cdts_vic_j1(): #Vérification si le J1 'X' a gagné, lignes, diagonales,colonnes.
    global result
    if all(cell=='X' for cell in board[0:3]): #all() vérifie si chaque variable est égale, dans ce cas, à 'X'
        result=1 #Définis l'état de la partie comme Victoire pour J1 'X'
        
    elif all(cell=='X' for cell in board[3:6]):
        result=1
        
    elif all(cell=='X' for cell in board[6:9]):
        result=1
        
    elif board[0]==board[4]==board[8]=='X':
        result=1
        
    elif board[2]==board[4]==board[6]=='X':
        result=1
        
    elif board[0]==board[3]==board[6]=='X':
        result=1
        
    elif board[1]==board[4]==board[7]=='X':
        result=1
        
    elif board[2]==board[5]==board[8]=='X':
        result=1
        
    

def cdts_vic_j2(): #Vérification si le J1 'X' a gagné, lignes, diagonales,colonnes.
    global result
    if all(cell=='O' for cell in board[0:3]):
        result=2 ##Définis l'état de la partie comme Victoire pour J2 'O'
        
    elif all(cell=='O' for cell in board[3:6]):
        result=2
        
    elif all(cell=='O' for cell in board[6:9]):
        result=2
        
    elif board[0]==board[4]==board[8]=='O':
        result=2
        
    elif board[2]==board[4]==board[6]=='O':
        result=2
        
    elif board[0]==board[3]==board[6]=='O':
        result=2
        
    elif board[1]==board[4]==board[7]=='O':
        result=2
        
    elif board[2]==board[5]==board[8]=='O':
        result=2
        
    
    

def draw():#Vérifies que toutes les cases ont été jouées et qu'aucun joueur n'a gagné la partie donc, qu'il y a eu match nul.
    global result
    if all(cell!=' ' for cell in board) and result!=1 and result!=2:
        result=0 #Définis l'état de la partie comme Match Nul.
        


while True: #Boucle qui fait tourner le jeu jusqu'à la victoire ou match nul
    if result=='ingame':    #Appel des fonctions dans l'ordre nécessaire au fonctionnement du jeu.
        plateau_jeu()
        movedujoueur()
        cdts_vic_j1()
        cdts_vic_j2()
        draw()
    elif result==1:
        plateau_jeu()
        print('GG WP J1')
        break #Victoire du J1, Fin de partie, fin du programme
    elif result==2:
        plateau_jeu()
        print('GG WP J2')
        break #Victoire du J2, Fin de partie, fin du programme
    elif result==0:
        plateau_jeu()
        print('Belle partie,\nMatch nul')
        break #Match nul, Fin de partie, fin du programme