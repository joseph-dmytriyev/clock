import time
from datetime import datetime, timedelta

Heure1 = " %H:%M:%S "


current_time = datetime.now()
alarm = None


def horloge():
    global current_time, alarm
    while True:
        display_hour()
        if alarm and current_time.strftime(Heure1) == alarm.strftime(Heure1):
            print("\n*** Alarme ! Il est", alarm.strftime(Heure1), "***")
            alarm = None
        time.sleep(1)
        current_time += timedelta(seconds=1)

def display_hour():
    print(current_time.strftime(Heure1), end="\r")
#------------------haytham-------------------------------

def set_time(heure_tuple):
    global current_time
    heures, minutes, secondes = hour_tuple
    current_time = current_time.replace(hour=heures, minute=minutes, second=secondes)


#-------------------Josph-----------------------------------------
def set_alarm(heure_tuple):
    global alarm
    heures, minutes, secondes = hour_tuple
    alarm = datetime.now().replace(hour=heures, minute=minutes, second=secondes)

def time_stop():

    global pause
    pause = not pause
    if pause:
        print("\nHorloge mise en pause.")
    else:
        print("\nHorloge reprise.")

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
        set_alarm((heures, minutes, secondes))
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
        set_time((heures, minutes, secondes))
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
  

