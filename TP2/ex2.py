def premier(nbr):
    if nbr < 2:
        return False
    for i in range(2, int(nbr**0.5) + 1):
        if nbr % i == 0:
            return False
    return True

def nbr_premier(m, n):
    return [x for x in range(m, n + 1) if premier(x)]
print(nbr_premier(10, 20))

