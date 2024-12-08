x = [1,2,3]
y = x
print(y)

x[1] = -15
print(x)
print(y)

x = [1,2,3]
y = x[:]
x[1] = -15
print(x)
print(y)