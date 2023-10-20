jour=0
heure=0
minute=0
print("saisir un jour (0-30) :")
jour=int(input())
print("saisir un heure (0-24) :")
heure=int(input())
print("saisir un minute (0-60) :")
minute=int(input())
minute=(jour*24*60)+(heure*60) + minute
print("le nombre de minute ecoulé depuis le début du moi est de :", minute)