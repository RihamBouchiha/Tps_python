import time
from datetime import datetime
class Employe:
    def __init__(self,matricule,nom,prenom,dateNaissance,dateEmbauche,salaire):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        self.dateEmbauche = dateEmbauche
        self.salaire = salaire
    
    def age(self):
        t=datetime.today() 
        return (t - self.dateNaissance)
        
    def anciente (self):
        t = datetime.today()
        return (t - self.dateEmbauche)
    
    def augmentationDuSalaire(self,an):
        if an < 5:
            self.salaire /= 0.02
        elif an <10 and an > 5 :
            self.salaire /= 0.05
        else:
            self.salaire /= 0.1
        
    def afficherEmploye(self,ancientee,augmentation):
        
        print(f"la matricule de l'employé est:{self.matricule}")
        print(f"le nom  de l'employé est:{self.nom}")
        print(f"le prenom de l'employé est:{self.prenom}")
        print(f"l'acienneté de l'employé est:{ancientee}")
        print(f"le salaire augmenté de l'employé est:{augmentation}")   


emp = Employe(1,"bou","riham",2003,2021,6000000)
x = emp.anciente()
y = emp.augmentationDuSalaire(x)
emp.afficherEmploye(x,y)          







    
