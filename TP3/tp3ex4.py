def factorielle_for(n):
    resultat = 1
    print(f"Calcul de la factorielle de {n} avec une boucle 'for':")

    for i in range(1, n + 1):
        resultat *= i
        print(f"{n}! = {resultat}")

    return resultat

def factorielle_while(n):
    resultat = 1
    i = 1
    print(f"Calcul de la factorielle de {n} avec une boucle 'while':")

    while i <= n:
        resultat *= i
        print(f"{n}! = {resultat}")
        i += 1

    return resultat

n = int(input("Entrez un entier n pour calculer n! : "))

choix_boucle = int(input("Choisissez la boucle (1 pour 'for' ou 2 pour 'while') : "))

if choix_boucle == 1:
    resultat = factorielle_for(n)
elif choix_boucle == 2:
    resultat = factorielle_while(n)
else:
    print("Choix de boucle non valide. Veuillez choisir 1 pour 'for' ou 2 pour 'while'.")
    resultat = None

if resultat is not None:
    print(f"Le résultat final de {n}! est : {resultat}")