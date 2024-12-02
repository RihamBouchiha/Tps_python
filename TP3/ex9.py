def estdistinct(nb) :
    string_nb = str(nb)
    if len(set(string_nb)) == len(string_nb) :
        print ("le nombre que vous avez saisi est distinct")
    else:
        print("le nombre contient des doublons")

nb = int(input("saisissez votre nombre:"))
distinct_nbr = estdistinct(nb)
