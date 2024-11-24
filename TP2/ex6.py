try:
    password = input ("saisissez votre mot de passe : ")
    if len(password) >=8:
        raise ValueError("le mot de passe ne doit pas dépasser 8 caractères")
    if " " in password :
        raise ValueError(" le mot de passe ne doit pas contenir de l'espace")
    else:
        input ("mot depasse validé")
except ValueError as e :
    print (f"Vous avez une erreur : {e}")