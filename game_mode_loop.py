""""
Créer un menu qui donnera 3 choix :
1 PVP
2 PVE
3 
"""


while True:
    Game_mode = str(input("Quel mode souahitez vous jouer ?\nVous avez le choix entre ces deux modes : \n \
                          Tapez PVP pour jouer contre un autre joueur \n \
                          Tapez PVE pour jouer contre une intelligence artificielle \nTapez Q pour quitter. \n Quel choix faites vous? : "))
    
    if Game_mode == "PVP":
        # Appeler la fonction pour le mode PVP
        mode_PVP()
        break
    elif Game_mode == "PVE":
        # Appeler la fonction pour le mode PVE
        mode_PVE()
        break
    elif Game_mode == "Q":
        print("Merci d'avoir joué ! À bientôt.")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")






