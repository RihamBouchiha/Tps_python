temps = int(input("Saisissez le temps en secondes : "))

heure = temps // 3600                     
minute = (temps % 3600) // 60             
seconde = temps % 60                       
print(f"Heure : {heure} H {minute} m {seconde} S")
