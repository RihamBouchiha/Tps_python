def second_max(L):
    liste1 = list(set(L))  
    liste1.sort()  
    if len(liste1) > 1:
        return liste1[-2]  
    else:
        return None  

L = [1, 2, 3, 4, 5]
print(second_max(L)) 
