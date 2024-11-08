"""""
Cap=float(input("Quel est l'investissement initial? :"))               # cap = capital rend = rendement
Rend=float(input("Quel est le rendement initial ? :"))

Cap_fin=Cap*(1+(Rend/100))              
Gain=Cap_fin-Cap

while True:

    Cap_fin=Cap*(1+(Rend/100))
    Gain=Cap_fin-Cap                            #\n = retour à la ligne

    suite=input("Bienvenue dans votre espace d'investissement\nComment puis-je vous aider?\nTapez '1' pour gérer votre solde\nTapez '2' pour modifier le rendement\nTapez '3' pour consulter votre solde\nTapez 'K' pour vous déconnecter")
    if suite=="1":
        Nv_Inv=float(input("Combien voulez-vous investir ou retirer"))
        Cap=Nv_Inv+Cap
        print("Très bien, votre nouveau solde est de {}€".format(Cap))

    if suite=="2":
        Nv_Rend=float(input("De combien de pourcentages est-ce-que le rendement change-t-il?"))
        Rend=Nv_Rend+Rend
        print("Très bien, le nouveau rendement est de {}%".format(1+(Rend)/100))

    if suite=="3":
        print("Votre solde est acutellement de {}€\nLe rendement annuel est de {}%\nVotre solde en fin d'année est estimé à {}€\nVos gains estimés à la fin de l'année sont de {}€".format(Cap,Rend,Cap_fin,Gain))

    if suite=="K":
        break
        
GPT : """

Cap = float(input("Quel est l'investissement initial? :"))  # capital initial
Rend = float(input("Quel est le rendement initial ? :"))    # rendement initial en pourcentage

# Calcul initial du capital final et du gain
Cap_fin = Cap * (1 + (Rend / 100))
Gain = Cap_fin - Cap

while True:
    # Message d'accueil et menu
    suite = input("\nBienvenue dans votre espace d'investissement\n"
                  "Comment puis-je vous aider?\n"
                  "Tapez '1' pour gérer votre solde\n"
                  "Tapez '2' pour modifier le rendement\n"
                  "Tapez '3' pour consulter votre solde\n"
                  "Tapez 'K' pour vous déconnecter : ")
    
    if suite == "1":
        # Option pour investir ou retirer de l'argent
        Nv_Inv = float(input("Combien voulez-vous investir ou retirer ? : "))
        Cap += Nv_Inv  # Mise à jour du capital
        Cap_fin = Cap * (1 + (Rend / 100))  # Recalcule Cap_fin avec le nouveau Cap
        Gain = Cap_fin - Cap  # Recalcule le gain
        print("Très bien, votre nouveau solde est de", round(Cap, 2), "€")

    elif suite == "2":
        # Option pour modifier le rendement
        Nv_Rend = float(input("De combien de pourcentage est-ce que le rendement change-t-il ? : "))
        Rend += Nv_Rend  # Mise à jour du rendement
        Cap_fin = Cap * (1 + (Rend / 100))  # Recalcule Cap_fin avec le nouveau rendement
        Gain = Cap_fin - Cap  # Recalcule le gain
        print("Très bien, le nouveau rendement est de", round(Rend, 2), "%")

    elif suite == "3":
        # Option pour consulter le solde
        print("Votre solde est actuellement de", round(Cap, 2), "€")
        print("Le rendement annuel est de", round(Rend, 2), "%")
        print("Votre solde en fin d'année est estimé à", round(Cap_fin, 2), "€")
        print("Vos gains estimés à la fin de l'année sont de", round(Gain, 2), "€")

    elif suite == "K":
        # Option pour se déconnecter
        print("Déconnexion en cours. Merci d'avoir utilisé notre service.")
        break

    else:
        print("Choix invalide, veuillez réessayer.")