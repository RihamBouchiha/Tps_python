def rotation(L):
    if L:  
        L.insert(0, L.pop())  
    return L

L = [1, 2, 3, 4]
print(rotation(L))  
