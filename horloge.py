import time
from datetime import datetime, timedelta

class Horloge:
    def __init__(self, heures=0, minutes=0, secondes=0, mode_12_heures=False):
        self.heure_actuelle = timedelta(hours=heures, minutes=minutes, seconds=secondes)
        self.alarme = None
        self.mode_12_heures = mode_12_heures

    def afficher_heure(self):
        #Affiche l'heure actuelle au format 12 heures ou 24 heures
        heures, reste = divmod(self.heure_actuelle.seconds, 3600)
        minutes, secondes = divmod(reste, 60)
        
        if self.mode_12_heures:
            periode = "AM" if heures < 12 else "PM"
            heures_12 = heures % 12 or 12  # Convertit 0 en 12 pour le mode 12 heures
            print(f"{heures_12:02}:{minutes:02}:{secondes:02} {periode}", end='\r')
        else:
            print(f"{heures:02}:{minutes:02}:{secondes:02}", end='\r')

    def regler_heure(self, heures, minutes, secondes):
        #Règle l'heure actuelle.
        self.heure_actuelle = timedelta(hours=heures, minutes=minutes, seconds=secondes)
        print("\nHeure réglée avec succès.")

    def regler_alarme(self, heures, minutes, secondes):
        #Règle l'alarme.
        self.alarme = timedelta(hours=heures, minutes=minutes, seconds=secondes)
        print("\nAlarme réglée avec succès.")

    def verifier_alarme(self):
        #Vérifie si l'heure actuelle correspond à l'alarme.
        if self.alarme and self.heure_actuelle == self.alarme:
            print("\n⏰ Alarme ! Il est l'heure !")
            self.alarme = None  # Désactive l'alarme après déclenchement

    def changer_mode_affichage(self, mode_12_heures):
        #Change le mode d'affichage de l'heure (12 heures ou 24 heures).
        self.mode_12_heures = mode_12_heures
        mode = "12 heures" if mode_12_heures else "24 heures"
        print(f"\nMode d'affichage changé : {mode}.")

    def demarrer(self):
        #Démarre l'horloge.
        try:
            while True:
                self.afficher_heure()
                self.verifier_alarme()
                time.sleep(1)
                self.heure_actuelle += timedelta(seconds=1)
        except KeyboardInterrupt:
            print("\nHorloge arrêtée.")

# Exemple d'utilisation
horloge = Horloge(16, 30, 0)
horloge.changer_mode_affichage(False)  # Active le mode 12 heures
horloge.regler_alarme(16, 30, 5)  # Régler l'alarme à 16:30:05
horloge.demarrer()
