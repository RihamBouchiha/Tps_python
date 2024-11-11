  
def div_com(m,n):
    try:
        div_m = {i for i in range(1,m+1) if m%i ==0}
        div_n= {i  for i in range(1,n+1) if n%i ==0}
        return sorted (div_n & div_m)
    except TypeError:
        print("saisssez un npmbre entier!!!")

print(div_com(18,27))


