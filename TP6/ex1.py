def indices_max(L):
    maximum = max(L)
    indices = [i for i, x in enumerate(L) if x == maximum]
    return maximum, indices

Liste = [1, 2, 3, 3, 2, 1]
print(indices_max(Liste))  
