def est_premier(n):
    """Vérifie si n est un nombre premier."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nombres_premiers_jumeaux(limite):
    """Renvoie une liste des couples de nombres premiers jumeaux inférieurs ou égaux à 'limite'."""
    jumeaux = []
    dernier_premier = None  
    
    for n in range(2, limite + 1):
        if est_premier(n):
            if dernier_premier and n - dernier_premier == 2:
                jumeaux.append((dernier_premier, n))
            dernier_premier = n  
    
    return jumeaux

jumeaux = nombres_premiers_jumeaux(1000)
print("Les nombres premiers jumeaux inférieurs ou égaux à 1000 sont :")
print(jumeaux)
