data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008' 

email = data.split()[1]

adr  = email.split('@')[1]

print(adr)