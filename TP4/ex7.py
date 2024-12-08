def remplacement (chaine):
    chaine_not = chaine.find("not")
    chaine_poor = chaine.find("poor")

    if chaine_not != -1 and chaine_poor != -1 and chaine_not < chaine_poor:
         chaine = chaine[:chaine_not] + 'good' + chaine[chaine_poor+4:]
    
    return chaine
print(remplacement("the exercice is not that poor"))