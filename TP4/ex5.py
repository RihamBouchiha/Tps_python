def trouver_indice(chaine, caractere):
    indices = []
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            indices.append(i)
    return indices

resultat = trouver_indice("je m'appellllll", "l")
print(resultat)
