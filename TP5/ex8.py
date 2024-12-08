def cumul(liste):
    cumul = []
    total = 0
    for i in liste:
        total += i
        cumul.append(total)
    return cumul

print(cumul([1, 4, 7]))  

