import math

def calcul_variance(numbers):
    """
    Calcule la variance d'une série de nombres.
    
    Paramètres :
    - numbers (tuple) : Un tuple de nombres
    
    Retourne :
    - La variance (float)
    """
    if not numbers:
        return 0
    
    n = len(numbers)  
    moyenne = sum(numbers) / n  
    variance = sum((x - moyenne) ** 2 for x in numbers) / n  # Formule de la variance
    
    return variance

def calcul_ecart_type(numbers):
    """
    Calcule l'écart-type d'une série de nombres.
    
    Paramètres :
    - numbers (tuple) : Un tuple de nombres
    
    Retourne :
    - L'écart-type (float)
    """
    variance = calcul_variance(numbers)
    return math.sqrt(variance)

valeurs = (11, 10, 16, 12, 15, 19, 12, 9, 11, 16, 20, 20, 11, 13, 18, 10, 16, 20, 10, 14, 10, 14, 7, 17, 9, 9, 14, 19, 10, 19, 18, 9)

variance = calcul_variance(valeurs)
ecart_type = calcul_ecart_type(valeurs)

print(f"Variance : {variance:.2f}")
print(f"Écart-type : {ecart_type:.2f}")
