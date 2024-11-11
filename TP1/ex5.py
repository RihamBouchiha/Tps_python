try:
    n = int(input("Saisissez le nombre de termes de la suite de Fibonacci à afficher : "))
    while n<0:
        n = int(input("Saisissez un nombre qui est sup a 0 : "))

    
    a, b = 0, 1
    for _ in range(n):               
        print(a, end=" ")  
        a, b = b, a + b
    
except ValueError :
    print(f"Veuillez entrer un nombre entier positif.")
