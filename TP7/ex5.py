def comptage(mot):
    """
    Compte les occurrences de chaque caractère dans un mot.

    Paramètres :
    - mot (str) : Un mot en lettres capitales non accentuées.

    Retourne :
    - dict : Un dictionnaire avec les caractères comme clés et leurs occurrences comme valeurs.
    """
    resultat = {}
    for lettre in mot:
        if lettre in resultat:
            resultat[lettre] += 1
        else:
            resultat[lettre] = 1
    return resultat

# Test de la fonction
mot_test = "PROGRAMMATION"
print(f"Occurrences dans '{mot_test}' : {comptage(mot_test)}")
