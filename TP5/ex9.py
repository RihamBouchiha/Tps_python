def moyenne(moy_notes):
    moyennes = {}
    for eleve, notes in moy_notes.items():
        if notes:  
            moyennes[eleve] = sum(notes) / len(notes)
        else:
            moyennes[eleve] = 0  
    return moyennes

eleves = {
    "riham": [15, 14, 13],
    "siham": [10, 12, 11],
    "issam": [8, 9, 10]
}
print(moyenne(eleves))  
