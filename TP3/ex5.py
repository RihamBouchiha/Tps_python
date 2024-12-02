def del_space(chaine):
    new_chaine =""
    for i in range(len(chaine)):
        if chaine[i]!=" ":
            new_chaine +=chaine[i]
    return new_chaine

####################

ch = input("saisissez une chaine svp:")
chaine_new = del_space(ch)
input (f"la nouvelle chaine est:{chaine_new}")