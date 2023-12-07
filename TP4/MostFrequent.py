L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
L=[]
x = 0
y = 0
for i in range(len(L1)):
    n = 0
    for j in range(len(L1)):
        if L1[i] == L1[j]:
            n+=1
            L.append([L1[i], n])
print(L)
for k in range(len(L)):
    if L[k][1] > x:
        x = L[k][0]
        y = L[k][1]

print(f"Le nombre le plus frequent dans la liste est le : {x} ({y} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
