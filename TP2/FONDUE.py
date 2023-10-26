BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) convivées à la fondue : "))
NouvelleQuantite = nbConvives / BASE
fromage = fromage * NouvelleQuantite
eau = eau * NouvelleQuantite
ail = ail * NouvelleQuantite
pain = pain*NouvelleQuantite
print("Pour faure une fondue fribourgeoise pour ", nbConvives, " il vous faut : \n -", fromage, "gr de fromage \n -", eau, "dl d'eau \n -",ail, "gousse(s) \n -", pain, "gr de pain")