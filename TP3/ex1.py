#fonction pour calculer le cube

def cube(arg):
    return (arg * arg * arg)
res = cube(2)
print (f"le cube du nombre est : {res}")

#fonction pour calculer le volume sphère

def VolumeSphere(r):
    return((4*3.14*cube(r))/3)
res1 = VolumeSphere(6)
print(f"le VolumeSphere du nombre est: {res1}")

