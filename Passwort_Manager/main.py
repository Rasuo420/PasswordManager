"""
Projekt : Passwort Manager mit GUI
Gruppe: Leon, Julian und Luca
Erstelldatum: 12.03.25


Programm soll folgendes können:
- Verschiedene User mit verschiedenen Passwörtern
- Usergruppen (Admin, Solo User ohne Gruppe, Gruppenuser (teilen sich Passwörter)
- Hidden Passwörter
- An und Abmelden
- Bearbeiten, löschen und hinzufügen von Passwörtern
- Erstellen von Usern
- Interaktives Design (inspiriert von Bitwarden)
- Hosted auf einem Server
- Datenbank dafür wird mySQL sein
- GUI soll auf basis von PyQt sein




Main Programm mit den aufrufen der einzelnen Classen
"""

from GUI import *
from Classes import *


window()


User("Luca",12,True)







