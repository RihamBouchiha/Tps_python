class Etudiant:
    id = 1
    repertoire = []

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.eid = Etudiant.id
        Etudiant.id += 1
        Etudiant.repertoire.append(self)


et1 = Etudiant("Dupont", "Jean")
et2 = Etudiant("Dupont", "Jean")

print(f"{et1.nom} {et1.prenom}, numéro d'étudiant : {et2.eid}")
print(Etudiant.repertoire)
