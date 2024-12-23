class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    def __str__(self):
        return f"Nom: {self._nom}, Age: {self._age}"


class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self._salaire = salaire

    def show_salary(self):
        print("salry is:", self._salaire)


class Manager(Employe):
    def show_salary(self):
        print("salry is:", self._salaire)


p = Personne("riham", 21)
e = Employe("issam", 22, 50000)
m = Manager("siham", 23, 2100)
print(p)
print(e)
m.show_salary()
e.show_salary()
