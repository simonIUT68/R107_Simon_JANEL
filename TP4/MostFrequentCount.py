L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
L=[]
x = 0
y = 0
z = 0
for i in range(len(L1)):
    x = L1.count(L1[i])
    if x > y:
        y = x
for r in range(len(L1)):
    x = L1.count(L1[r])
    if y == x:
        z = L1[r]
        print(f"Le nombre le plus frequent dans la liste est le : {z} ({y} x)")
        break

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
