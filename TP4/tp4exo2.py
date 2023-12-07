# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;

# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
moy = 0
a = 0
for i in range(nombreEtudiants):
    a = float(input(f"Entrer la note de l étudiant {i} : "))
    if a <= 20 and a >= 0:
        notes.append(a)
    while a < 0 and a > 20:
        print("entrer un nombre entre 0 et 20 !")
        a = float(input(f"Entrer la note de l étudiant {i} : "))
        if a <= 20 and a >= 0:
            notes.append(a)
for j in range(len(notes)):
    moy = notes[j] + moy

print(moy/len(notes))

print("Numéro de l'Etudiant | note | ecart à la moyenne")
for z in range(nombreEtudiants):
    a = (notes[z] - (moy/len(notes)))
    print(z, "|", notes[z], "|", a)