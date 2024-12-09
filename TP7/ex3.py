moyennes_T1={
    "Celestine" : 11, "cedric" : 10, "Farida" : 16, "zelie" : 12 ,"Fatoumata" : 15,
    "colombin" : 19, " Opheline": 12 , "Gauvin" : 9 ,"Rodolphe" : 11, "Ariel" : 16,
    "perrine" : 20 ,"hippolvte" : 20 ,"delphine" :11,"bertrand":13, "Awa" : 18,
    "perrette":10, "eulalie" :16 ,"moussa" :20 ,"issa" :10, "marceline" :14,
    "bernabe":10,"leonce" :14,"everise":7,"jean":17 ,"anceline" :9,
    "leontine":9,"maya":14,  "pablo" :19,"bernard":10, "vinciane":19,
    "daphne" :18, "Ludovic":9
}

def _rechercheeleve(nom):
    if nom in moyennes_T1.keys():
        print(nom,"est dans la classe")
    else:
        print(f"{nom} n'est pas dans la classe")
        
_rechercheeleve("Ludovic")