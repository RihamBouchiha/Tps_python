def capitalize(chaine):
    mots = chaine.split()
    if mots :
        mot_un = mots[0]
        return mot_un.capitalize()
    
ch = input("saisissez votre chaine svp:")
chaine_capitalize = capitalize(ch)
if chaine_capitalize :
    print(f"chaine capitalisé:{chaine_capitalize}")    
else:
    print("vous n'avez saisi aucune phrase")

