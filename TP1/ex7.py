while True:
    try:
        N = int(input("Entrez un entier N strictement positif et supérieur à 100 : "))
        if N > 100:
            break
        else:
            print("Le nombre doit être strictement supérieur à 100.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

S = N
while S >= 10:
    tmp = 0
    while S > 0:
        tmp += S % 10  
        S = S // 10                
    S = tmp             

print(f"Le code est :{tmp}{N}")
