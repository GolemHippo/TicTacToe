Cap=float(input("Quel est l'investissement initial"))               # cap = capital rend = rendement
Rend=float(input("Quel est le rendement initial"))

Cap_fin=Cap*(1+(Rend/100))              
Gain=Cap_fin-Cap

while True:

    Cap_fin=Cap*(1+(Rend/100))
    Gain=Cap_fin-Cap

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
        