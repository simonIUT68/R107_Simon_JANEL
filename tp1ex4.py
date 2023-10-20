jour=0
heure=0
date=0
minute=0
print("entrez le nomnbre de minute depuis le début du mois (0-44700) :")
minute=int(input())
jour = int(minute/1440)
minute = minute%1440
heure = int(minute/60)
minute = int(minute%60)
print("On est le {:.0f}".format(jour),"à {:.0f} heure et".format(heure)," {:.0f} minutes".format(minute))