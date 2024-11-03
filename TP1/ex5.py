try:
        n = int(input("Saisissez le nombre de termes de la suite de Fibonacci à afficher : "))

    if n <= 0:
        raise ValueError("Le nombre doit être positif.")
    a, b = 0, 1

    print("Les premiers", n, "termes de la suite de Fibonacci sont :")

    for _ in range(n):
        print(a, end=" ")  
        a, b = b, a + b    
except ValueError as e:
    print(f"Erreur : {e}. Veuillez entrer un nombre entier positif.")
