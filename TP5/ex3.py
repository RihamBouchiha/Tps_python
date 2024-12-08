liste = [17,38,10,25,72,-1,16,82,0,5]

liste.sort()
print(liste)

liste.append(12)
print(liste)

liste.reverse()
print(liste)

indice_17 = liste.index(17)
print(indice_17)

liste.remove(38)
print(liste)

sous_liste = liste[1:3]
print(sous_liste)

sous_liste_debut = liste[:2]
print(sous_liste_debut)

sous_liste_3 = liste[2:]
print(sous_liste_3)

sous_liste_complete = liste[:]
print(sous_liste_complete)

premier_dernier = (liste[0], liste[-1])
print(premier_dernier)