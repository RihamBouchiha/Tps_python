try:
    n = int(input("Saisissez un nombre entier positif n : "))

    if n <= 0:
        raise ValueError("Le nombre doit être positif.")
    somme = 0
    for i in range(1, n + 1):
        somme += i
    print(f"La somme des nombres de 1 à {n} est : {somme}")
except ValueError:
    print(f" Veuillez entrer un nombre entier positif.")
