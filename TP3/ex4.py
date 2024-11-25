def nbr_voyelle(chaine):
    compteur =0
    for i in range(len(chaine)):
        if chaine[i] == 'a':
            compteur +=1
        
        elif chaine[i] == 'e':
            compteur +=1

        elif chaine[i] == 'o':
            compteur +=1

        elif chaine[i] == 'u':
            compteur +=1
         
        elif chaine[i] == 'i':
            compteur +=1

        elif chaine[i] == 'y':
            compteur +=1

    return compteur

ch = input("saisissez la chaine svp:")

chaine = nbr_voyelle(ch)
print (f"le nombre de voyelles dans la chiane que vous avez saisi est : {chaine}")

        

