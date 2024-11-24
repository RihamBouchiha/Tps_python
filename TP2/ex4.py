from_doll_to_eur = 0.85
from_doll_to_grp = 0.75
from_doll_to_jpy = 110.0
devise = 0
montant_grp = 0
montant_euro = 0
montant_jpy = 0

montant = float(input("Saisissez votre montant en dollar svp: "))
devise = int(input("Saisissez la devise (1 pour EUR, 2 pour GRP, 3 pour JPY): "))

if devise == 1:
    montant_euro = montant * from_doll_to_eur
    print(f"Votre montant en EURO est : {montant_euro}")
elif devise == 2:
    montant_grp = montant * from_doll_to_grp
    print(f"Votre montant en GRP est : {montant_grp}")
elif devise == 3:
    montant_jpy = montant * from_doll_to_jpy
    print(f"Votre montant en JPY est : {montant_jpy}")
else:
    print("Devise non valide. Veuillez saisir 1 pour EUR, 2 pour GRP ou 3 pour JPY.")
