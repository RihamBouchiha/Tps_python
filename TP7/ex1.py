dico_fr_en = {
    'un':'one',
    'arbre':'tree',
    'chat':'cat',
    'chien':['dog','siham'],
    'nuage':'cloud',
    'pere':'father',
    'mere':'mother',
    'nuage':'cloud',
    'fleur' : 'flower',
    'jardin':'garden'
}

def traduction(key):
    if key in dico_fr_en:
        return (dico_fr_en.get(key))

print("les mots que je peux traduire en anglais sont:",dico_fr_en.keys())
mot = input ("saisissez lemot que vous souhaitez traduire:")
print("la traduction du mot que vous avez saisi est:",traduction(mot))