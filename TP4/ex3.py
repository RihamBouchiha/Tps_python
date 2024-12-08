chaine = "rihamsihamissam"
new_liste = []
for i in range (0,len(chaine),5):
        frag=chaine[i:i+5]
        frag_rev=frag[::-1]
        new_liste.append(frag_rev)

print(new_liste)
                