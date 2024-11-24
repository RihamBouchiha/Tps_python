a = int(input(f"saisissez le 1er nbr:"))
b=int(input(f"saisissez le 2eme nbr:"))
while b!=0:
    a,b = b, a%b
print("le PGCD des 2 nbrs saisies est:",a)