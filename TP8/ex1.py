class Compte:
    def __init__(self,nom,num,balance):
        self.__nom = nom
        self.num = num
        self.__balance = balance
    
    #setter pour NOM
    def setNom(self,nom):
        self.__nom = nom

    #getter pour NOM
    def getNom(self):
        return self.__nom
    
    #setter pour NUMERO
    def setNumero(self,num):
        self.num = num

    #getter pour NUMERO

    def getNumero(self):
        return self.__num
    
    #setter pour BALANCE
    def setBalance(self,balance):
        self.__balance = balance

    #getter pour BALANCE

    def getBalance(self):
        return self.__balance


    #methode deposer
    def deposer(self,som):
         self.__balance += som
         print(f"la somme que vous avez ajouté est:{som}")

#methode pour retirer
    def retirer(self,min):
        self.__balance -= min
        print(f"la somme que vous avez retirer est : {min}")
        
client = Compte("Asmaa",1234,20000)

depot = client.deposer(3000)

client.retirer(800)

total = client.getBalance()
nom = client.getNom()
print (f"la somme totale de {nom} est:{total}")