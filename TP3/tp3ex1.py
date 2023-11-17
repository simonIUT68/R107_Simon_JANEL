#A
N = int(input("Entrez la valeur de N : "))
somme = 0
i = 0

while i <= N:
    somme += i
    i += 1

print("La somme des N premiers entiers naturels est :", somme)

#B
valeur_utilisateur = int(input("Entrez une valeur (entre 0 et 100) : "))

while valeur_utilisateur != 100:
    valeur_utilisateur = int(input("Entrez une valeur (entre 0 et 100) : "))

print("La boucle d'attente se termine. Vous avez entré la valeur 100.")

#C
valeurs_inf_10 = 0
valeurs_10_a_15 = 0
valeurs_sup15 = 0

for  in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    while valeur < 0 or valeur > 20:
        print("La valeur doit être comprise entre 0 et 20.")
        valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    if valeur < 10:
        valeurs_inf_10 += 1
    elif valeur < 15:
        valeurs_10_a_15 += 1
    else:
        valeurs_sup_15 += 1

print("Le nombre de valeurs inférieures strictement à 10 est :", valeurs_inf_10)
print("Le nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15 est :", valeurs_10_a_15)
print("Le nombre de valeurs supérieures ou égales à 15 est :", valeurs_sup_15)

#D
X = float(input("Entrez un nombre supérieur à 1 (X) : "))

while X <= 1:
    print("Veuillez entrer un nombre supérieur à 1.")
    X = float(input("Entrez un nombre supérieur à 1 (X) : "))

somme = 0
N = 0

while somme <= X:
    N += 1
    somme += N

N -= 1

print("Le plus grand nombre N tel que la somme de 0 à N soit inférieure ou égale à", X, "est :", N)