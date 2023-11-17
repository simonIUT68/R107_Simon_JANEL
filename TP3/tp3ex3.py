import random

nombre_mystere = random.randint(0, 100)

print("Bienvenue dans le jeu de devinette !")
print("Essayez de deviner le nombre mystère entre 0 et 100.")

compteur_tours = 0

while True:
    guess = int(input("Entrez votre guess : "))

    compteur_tours += 1

    if guess < nombre_mystere:
        print("Le nombre mystère est plus grand. Essayez à nouveau.")
    elif guess > nombre_mystere:
        print("Le nombre mystère est plus petit. Essayez à nouveau.")
    else:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère {nombre_mystere} en {compteur_tours} tours.")
        break