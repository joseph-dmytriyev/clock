import time
from datetime import datetime, timedelta

Heure1 = " %H:%M:%S "


temps_courant = datetime.now()
alarme = None


def time_stop():

    global pause
    pause = not pause
    if pause:
        print("\nHorloge mise en pause.")
    else:
        print("\nHorloge reprise.")

def regler_heure(heure_tuple):
    global temps_courant
    heures, minutes, secondes = heure_tuple
    temps_courant = temps_courant.replace(hour=heures, minute=minutes, second=secondes)
#------------------haytham
def afficher_heure():
    print(temps_courant.strftime(Heure1), end="\r")
#-------------------Josph-----------------------------------------
def regler_alarme(heure_tuple):
    global alarme
    heures, minutes, secondes = heure_tuple
    alarme = datetime.now().replace(hour=heures, minute=minutes, second=secondes)

def horloge():
    global temps_courant, alarme
    while True:
        afficher_heure()
        if alarme and temps_courant.strftime(Heure1) == alarme.strftime(Heure1):
            print("\n*** Alarme ! Il est", alarme.strftime(Heure1), "***")
            alarme = None
        time.sleep(1)
        temps_courant += timedelta(seconds=1)

# Programme principal
print("     *** Menu ***     ")
print("1.Alarme ")
print("2.Régler Heure")
print("3.Horloge ")
print("4.Time Stop ")
answer0 = input(" : ").strip().lower()

if answer0 == "1":
    try:
        alarm_time = input("Entrez l'heure de l'alarme au format HH:MM:SS : ").strip()
        heures, minutes, secondes = map(int, alarm_time.split(":"))
        regler_alarme((heures, minutes, secondes))
        horloge()
    except ValueError:
        print("Format d'heure invalide. Veuillez entrer l'heure au format HH:MM:SS.")
    except KeyboardInterrupt:
        print("\nProgramme arrêté.")

#-----------------------------Haytham--------------------------------------------------------------

elif answer0 == "2" : 
   
    try:
        new_time = input("Entrez la nouvelle heure au format HH:MM:SS : ").strip()
        heures, minutes, secondes = map(int, new_time.split(":"))
        regler_heure((heures, minutes, secondes))
        print(f"Heure réglée à {heures:02}:{minutes:02}:{secondes:02}.")
        horloge()
    except ValueError:
        print("Format d'heure invalide. Veuillez entrer l'heure au format HH:MM:SS.")


elif answer0 == "3":
    try:
        print("Lancement de l'horloge ")
        horloge()
    except KeyboardInterrupt:
        print("\nProgramme arrêté.")



elif answer0 == "4":
    try:
        while True:
            horloge()
            input() 
            time_stop()
    except KeyboardInterrupt:
        print("\nProgramme terminé.")
  

