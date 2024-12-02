def compteur_mots(phrase):
    compteur =1
    for i in range(len(phrase)):
        if phrase[i] == " ":
            compteur+=1
    return compteur

ph = input("saisissez votre phrase svp:")
mots = compteur_mots(ph)
print(f"le nombre de mots dans votre phrase est {mots}")


"""def compteur_mots(phrase):
    mots = phrase.split()  
    return len(mots)      

ph = input("Saisissez votre phrase svp: ")
mots = compteur_mots(ph)
print(f"Le nombre de mots dans votre phrase est : {mots}")
"""
