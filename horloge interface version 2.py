# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 09:42:01 2025

@author: josep
"""

from datetime import datetime, timedelta
import customtkinter as ctk
from tkinter import messagebox  

class HorlogeApp:
    def __init__(self):
        self.nouvelle_heure = None
        self.temps_actuel = datetime.now()
        self.alarme = None  

        # Initialisation de l'interface
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.fenetre = ctk.CTk()
        self.fenetre.title("Horloge en temps réel avec alarme")
        self.fenetre.geometry("400x300")

        # Label pour afficher l'heure
        self.label = ctk.CTkLabel(self.fenetre, text="", font=("Helvetica", 32))
        self.label.pack(expand=True, pady=10)

        # Cadre pour les contrôles
        cadre_controles = ctk.CTkFrame(self.fenetre)
        cadre_controles.pack(pady=10)

        # Entrées pour l'heure, minute, seconde
        self.entre_heure = ctk.CTkEntry(cadre_controles, width=50, placeholder_text="HH")
        self.entre_minute = ctk.CTkEntry(cadre_controles, width=50, placeholder_text="MM")
        self.entre_seconde = ctk.CTkEntry(cadre_controles, width=50, placeholder_text="SS")
        self.entre_heure.pack(side="left", padx=5)
        self.entre_minute.pack(side="left", padx=5)
        self.entre_seconde.pack(side="left", padx=5)

        # Bouton pour modifier l'heure
        bouton_modifier = ctk.CTkButton(
            cadre_controles, text="Modifier l'heure", command=self.changer_heure
        )
        bouton_modifier.pack(side="left", padx=10)

        # Bouton pour régler l'alarme
        bouton_alarme = ctk.CTkButton(
            cadre_controles, text="Régler l'alarme", command=self.regler_alarme
        )
        bouton_alarme.pack(side="left", padx=10)

        # Lancer l'horloge
        self.heure_tps_reel()

    def changer_heure(self):
        #Change l'heure affichée
        try:
            heure = int(self.entre_heure.get())
            minute = int(self.entre_minute.get())
            seconde = int(self.entre_seconde.get())
            self.nouvelle_heure = (heure, minute, seconde)
        except ValueError:
            print("Veuillez entrer des nombres valides !")

    def regler_alarme(self):
        # Règle l'alarme à une heure spécifique
        try:
            heure = int(self.entre_heure.get())
            minute = int(self.entre_minute.get())
            seconde = int(self.entre_seconde.get())
            self.alarme = (heure, minute, seconde)
            print(f"Alarme réglée à : {heure:02}:{minute:02}:{seconde:02}")
        except ValueError:
            print(" entrer des nombres valides pour l'alarme !")

    def heure_tps_reel(self):
        #Met à jour l'heure en temps réel et vérifie l'alarme.
        if self.nouvelle_heure:
            self.temps_actuel = datetime.now().replace(
                hour=self.nouvelle_heure[0],
                minute=self.nouvelle_heure[1],
                second=self.nouvelle_heure[2],
            )
            self.nouvelle_heure = None
        else:
            self.temps_actuel += timedelta(seconds=1)

        self.label.configure(text=self.temps_actuel.strftime("%I:%M:%S %p"))

        # Vérifier si l'heure actuelle correspond à l'alarme
        if self.alarme:
            alarme_heure, alarme_minute, alarme_seconde = self.alarme
            if (
                self.temps_actuel.hour == alarme_heure
                and self.temps_actuel.minute == alarme_minute
                and self.temps_actuel.second == alarme_seconde
            ):
                self.declencher_alarme()

        self.label.after(1000, self.heure_tps_reel)

    def declencher_alarme(self):
        # Affiche un message lorsque l'alarme sonne.
        self.alarme = None  # fait en sorte que l'alarme ne se répète pas
        messagebox.showinfo("Alarme", "Il est temps !")
        print("Alarme déclenchée !")

    def run(self):
        """Lance l'application."""
        self.fenetre.mainloop()


if __name__ == "__main__":
    app = HorlogeApp()
    app.run()

