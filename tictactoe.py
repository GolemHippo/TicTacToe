cases = [" " for _ in range(9)] # Crées une liste, avec une boucle, composée de 9 variables vides :
#                                                              ' ' pour les 9 cases de la matrice.

joueur_actuel = 'X'                                                     # Définis le premier joueur comme le joueur 'X'.

resultat = 'en_jeu'                                                     # Définis l'état de la partie comme en cours.

signe ='O'

import random



def plateau_jeu():                             # Fonction affichant la matrice du jeu et chaque case grâce à la liste Cases. 
    
    print("", cases[0],"|", cases[1],"|", cases[2],"")
    print("---|---|---")
    print("", cases[3],"|", cases[4],"|", cases[5],"")
    print("---|---|---")
    print("", cases[6],"|", cases[7],"|", cases[8],"")


def move_du_joueur():                               # Places un 'X' ou un 'O' en alternance à chaque tour.
    
    case_jouee = int(input('Où voulez-vous jouez?'))                # Demandes au joueur sur quelle case il veut jouer.
    
    if 1 <= case_jouee <= 9:
        
        if cases[case_jouee-1] == ' ':                 # La liste commence à l'indexe 0 donc n-1 par rapport à la matrice. 
                                                                            # Vérifie que la case choisie est bien vide. 
                                       
            cases[case_jouee-1] = joueur_actuel     # Remplaces la variable correspondant à la case choisie par 'X' ou 'O'.
            
            change_de_joueur()          # Appelles la fonction "changedejoueur" pour changer de joueur après chaque coup.
            
        else:                                       # Si la case n'est pas vide alors elle a déjà été jouée.
            print('Vous devez choisir une bonne case, cette case a déja été jouée!!!')
            
    else:                               # Si la case choisie n'est pas entre 1 et 9 alors elle n'est pas valide.
        print(' Vous devez choisir une case comprise entre 1 et 9 !!!')


def change_de_joueur():                                     # Changes de joueur si l'autre joueur vient de jouer.
    
    global joueur_actuel            # Permet à la fonction de modifier à l'échelle globale la variable 'joueur_actuel'.
    
    joueur_actuel = 'O' if joueur_actuel == 'X' else 'X' # Si le joueur actuel est 'X' alors le prochain coup sera pour 'O'.


def ia(cases,signe):
    
    cases_vide = [i for i in range(len(cases)) 
                   if cases[i] is cases[i] == " "] 
    
    choix = random.choice(cases_vide)
    
    cases[choix] = signe
    
    change_de_joueur()


def move_du_joueur_vs_ia():                                     # Places un 'X' quand c'est le tour du joueur face à l'IA.
    
    if joueur_actuel == 'X':
        
        case_jouee = int(input('Où voulez-vous jouez?'))                # Demandes au joueur sur quelle case il veut jouer.
        
        if 1 <= case_jouee <= 9:
            
            if cases[case_jouee-1] == ' ':                  # La liste commence à l'indexe 0 donc n-1 par rapport à la matrice.
                                                                             # Vérifie que la case choisie est bien vide.
                                         
                cases[case_jouee-1] = 'X'                     # Remplaces la variable correspondant à la case choisie par 'X'.
                
                change_de_joueur()
                
            else:                                                    # Si la case n'est pas vide alors elle a déjà été jouée.
                print('Vous devez choisir une bonne case!!!')
                
        else:                                      # Si la case choisie n'est pas entre 1 et 9 alors elle n'est pas valide.
            print(' Vous devez choisir une case comprise entre 1 et 9 !!!')
            
    elif joueur_actuel == 'O':
        ia(cases,signe)
        


def conditionts_de_victoire_j1(): # Vérification si le J1 'X' a gagné, lignes, diagonales,colonnes.
    
    global resultat
    
    if all(cell == 'X' for cell in cases[0:3]): # all() vérifie si chaque variable est égale, dans ce cas, à 'X'
        
        resultat = 1 # Définis l'état de la partie comme Victoire pour J1 'X'
        
    elif all(cell == 'X' for cell in cases[3:6]):
        
        resultat = 1
        
    elif all(cell == 'X' for cell in cases[6:9]):
        
        resultat = 1
        
    elif cases[0] == cases[4] == cases[8] == 'X':
        
        resultat = 1
        
    elif cases[2] == cases[4] == cases[6] == 'X':
        
        resultat = 1
        
    elif cases[0] == cases[3] == cases[6] == 'X':
        
        resultat = 1
        
    elif cases[1]  ==  cases[4]  ==  cases[7]  ==  'X' :
        
        resultat = 1
        
    elif cases[2] == cases[5] == cases[8] == 'X':
        
        resultat = 1
    

def conditions_de_victoire_j2():                    # Vérification si le J2 ou l'IA 'O' a gagné, lignes, diagonales,colonnes.
    
    global resultat
    
    if all(cell == 'O' for cell in cases[0:3]) :
        
        resultat = 2                                        # Définis l'état de la partie comme Victoire pour J2 ou l'IA 'O'
        
    elif all(cell == 'O' for cell in cases[3:6]) :
        
        resultat = 2
        
    elif all(cell == 'O' for cell in cases[6:9]) :
        
        resultat = 2
        
    elif cases[0] == cases[4] == cases[8] == 'O' :
        
        resultat = 2
        
    elif cases[2] == cases[4] == cases[6] == 'O' :
        
        resultat = 2
        
    elif cases[0] == cases[3] == cases[6] == 'O' :
        
        resultat = 2
        
    elif cases[1] == cases[4] == cases[7] == 'O' :
        
        resultat = 2
        
    elif cases[2] == cases[5] == cases[8] == 'O' :
        
        resultat = 2
            

def egalite(): # Vérifies que toutes les cases ont été jouées et qu'aucun joueur n'a gagné la partie donc,qu'il y a eu match nul.
    
    if all(cell != ' ' for cell in cases) and resultat != 1 and resultat != 2:
        
        resultat = 0        # Définis l'état de la partie comme Match Nul.





def mode_pvp():
    
    while True: # Boucle qui fait tourner le jeu jusqu'à la victoire ou match nul
        
        if resultat  ==  'en_jeu' : # Appel des fonctions dans l'ordre nécessaire au fonctionnement du jeu.
            
            plateau_jeu()
            
            move_du_joueur()
            
            conditionts_de_victoire_j1()
            
            conditionts_de_victoire_j2()
            
            egalite()
            
        elif resultat  ==  1 :
            
            plateau_jeu()
            
            print('Félicitations à Joueur 1 pour la victoire')
            
            break # Victoire du J1, Fin de partie, fin du programme
        
        elif resultat  ==  2 :
            
            plateau_jeu()
            
            print('Félicitations à Joueur 2 pour la victoire')
            
            break # Victoire du J2, Fin de partie, fin du programme
        
        elif resultat  ==  0 :
            
            plateau_jeu()
            
            print('Belle partie,\nMatch nul')
            
            break # Match nul, Fin de partie, fin du programme


def mode_pve():
    
    while True: # Boucle qui fait tourner le jeu jusqu'à la victoire ou match nul
        
        if resultat == 'en_jeu': # Appel des fonctions dans l'ordre nécessaire au fonctionnement du jeu.
            
            plateau_jeu()
            
            move_du_joueur_vs_ia()
            
            conditionts_de_victoire_j1()
            
            conditionts_de_victoire_j2()
            
            egalite()
            
        elif resultat  ==  1 :
            
            plateau_jeu()
            
            print('Félicitations à Joueur 1 pour la victoire')
            
            break # Victoire du J1, Fin de partie, fin du programme
        
        elif resultat  ==  2 :
            
            plateau_jeu()
            
            print('Oh non... Désolé mais cette partie a été remportée par le robot !')
            
            break # Victoire de l'IA, Fin de partie, fin du programme
        
        elif resultat  ==  0 :
            
            plateau_jeu()
            
            print('Belle partie,\nMatch nul')
            
            break # Match nul, Fin de partie, fin du programme


while True:
    
    mode_de_jeu = str(input("Quel mode souhaitez vous jouer ?\nVous avez le choix entre ces deux modes : \n \
                          Tapez PVP pour jouer contre un autre joueur \n \
                          Tapez PVE pour jouer contre une intelligence artificielle \n \
                          Tapez Q pour quitter. \n Quel choix faites vous? : ")) # Input permettant de se déplacer dans le menu
    
    if mode_de_jeu  ==  "PVP":  #  Appeler la fonction pour le mode PVP
        
        mode_pvp()
        
        break
    
    elif mode_de_jeu  ==  "PVE": #  Appeler la fonction pour le mode PVE
        
        mode_pve()
        
        break
    
    elif mode_de_jeu  ==  "Q": #  Mettre fin au programme
        
        print("Merci d'avoir joué ! À bientôt.")
        
        break
    
    else: # En cas de choix invalide, permets de communiquer l'erreur à l'utilisateur
        
        print("Choix invalide. Veuillez réessayer.")
