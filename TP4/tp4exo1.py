print("Vous cherchez la table de multiplication de quel nombre ?")
a = float(input())
tab = []
for i in range(10):
    tab.append(a*i)
    print(a, "*", i," =", round(tab[i], 2))