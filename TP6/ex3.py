def suite(n):
    u = [0]  
    for i in range(n):
        u.append(2 * u[-1] + 1)
    return u

print(suite(5))  


def Somme_suite(n):
    u = suite(n) 
    return sum(u)

print(Somme_suite(5))  