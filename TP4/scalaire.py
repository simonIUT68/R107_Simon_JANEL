nMax = 3
v1 = []
v2 = []
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))
while n < 1 or n > 3:
    print("Entrez un nombre entre 1 et 3 !!")
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))
produit = 0
print("\nSaisie du premier vecteur : \n")
for i in range(n):
    a = int(input(f"v1[{i}] = "))
    v1.append(a)
print("Saisie du deuxième vecteur : \n")
for j in range(n):
    a = int(input(f"v2[{j}] = "))
    v2.append(a)
for k in range(n):
    produit = v1[k] * v2[k] + produit
print(f"\nLe produit scalaire de v1 par v2 vaut", float(produit))
