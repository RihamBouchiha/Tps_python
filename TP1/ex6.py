while True:
    try:
        prix_ht = float(input("Entrez le prix hors taxe : "))
        if prix_ht < 0:
            print("Le prix doit être un nombre positif.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre valide pour le prix.")

categorie = input("Entrez la catégorie de TVA (A, B ou C) : ")

if categorie == 'A':
    taux_tva = 0.07
elif categorie == 'B':
    taux_tva = 0.20
elif categorie == 'C':
    taux_tva = 0.25
else:
    print("Catégorie invalide.")
    taux_tva = None 
if taux_tva is not None:
    prix_ttc = prix_ht * (1 + taux_tva)
    print("Le prix toutes taxes comprises (TTC) est :", prix_ttc)
