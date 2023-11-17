heure_debut = int(input("Donnez l'heure de début de la location (un entier) : "))

if heure_debut < 0 or heure_debut > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
else:
    heure_fin = int(input("Donnez l'heure de fin de la location (un entier) : "))

    if heure_fin < 0 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !")
    elif heure_debut == heure_fin:
        print("Attention ! L'heure de fin est identique à l'heure de début.")
    elif heure_debut > heure_fin:
        print("Attention ! Le début de la location est après la fin.")
    else:
        duree_location = heure_fin - heure_debut

        cout_total = 0
        for heure in range(heure_debut, heure_fin):
            if heure < 7 or (heure >= 17 and heure < 24):
                cout_total += 1
            else:
                cout_total += 2

        print(f"Vous avez loué votre vélo pendant {duree_location} heure(s).")
        print(f"Le montant total à payer est de {cout_total:.1f} euro(s).")