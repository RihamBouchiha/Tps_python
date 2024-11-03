try : 
        entier= int(input("saisissez un nombre en entier svp:"))
        fac = entier 
        for i in range (1, entier):
           fac = (entier-1)*fac
        print("la factorielle de:",entier,"est:",fac)
except ValueError:
     print(input("saisissez un nombre en entier!"))
