def enlever_doublons(liste):
    res = []
    for i in liste:
        if i not in res:
            res.append(i)
    return res

doublons_liste = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

resultat = enlever_doublons(doublons_liste)

print(resultat)
