def livres_auteur(livres):
    auteurs = {}
    for livre in livres:
        auteur = livre['auteur']
        titre = livre['titre']
        if auteur not in auteurs:
           auteurs[auteur] = []
        auteurs[auteur].append(titre)
    return auteurs

livres = [
    
    {"titre": "la boite a merveilles", "auteur": "ahmed sefrioui"},
]
print(livres_auteur(livres))
