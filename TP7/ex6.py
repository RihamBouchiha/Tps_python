def est_premier(nombre):
    """
    Vérifie si un nombre est premier.
    """
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def trouver_tuples_premiers(n):
    """
    Trouve les tuples (p, q) de nombres premiers tels que p + q == n.
    
    Paramètres :
    - n (int) : La somme cible.

    Retourne :
    - list : Une liste de tuples (p, q).
    """
    tuples = []
    for p in range(2, n):  
        q = n - p 
        if est_premier(p) and est_premier(q) and p <= q:
            tuples.append((p, q))  
    return tuples


n = 20
print(f"Tuples (p, q) tels que p + q == {n} : {trouver_tuples_premiers(n)}")
