import mysql.connector # neue Bibliothek

Servername = '188.245.63.10' # Rechnername (localhost ist dein eigener Rechner)
Benutzer = 'test'
Passwort = '12341'
Datenbank = 'Namen'


# Verbindung mit der Datenbank
con = mysql.connector.connect(
    host=Servername,
    user=Benutzer,
    password=Passwort
)
con.database = Datenbank

# Funktion zum Hinzufügen eines Namens
def add_name(name):
    cursor = con.cursor()
    SQLBefehl = "INSERT INTO Namen (Namen) VALUES (%s)"
    cursor.execute(SQLBefehl, (name,))
    con.commit()
    print(f"Der Name '{name}' wurde erfolgreich in die Datenbank eingefügt.")
    cursor.close()

# Funktion zum Entfernen eines Namens
def remove_name(name):
    cursor = con.cursor()
    SQLBefehl = "DELETE FROM Namen WHERE Namen = %s"
    cursor.execute(SQLBefehl, (name,))
    con.commit()
    print(f"Der Name '{name}' wurde erfolgreich aus der Datenbank entfernt.")
    cursor.close()

# Funktion, um alle Namen aus der Datenbank anzuzeigen
def display_names():
    cursor = con.cursor()
    cursor.execute("SELECT Namen FROM Namen")
    row = cursor.fetchone()
    print("\nAktuelle Namen in der Datenbank:")
    while row is not None:
        print(row[0])  # Nur den Namen ausgeben
        row = cursor.fetchone()
    cursor.close()

# Benutzerinteraktion: Auswahl, ob Namen hinzugefügt oder entfernt werden soll
while True:
    print("\nWas möchtest du tun?")
    print("1. Namen hinzufügen")
    print("2. Namen entfernen")
    print("3. Alle Namen anzeigen")
    print("4. Beenden")

    choice = input("Gib die Zahl der gewünschten Aktion ein: ")

    if choice == '1':
        name_to_add = input("Gib den Namen ein, den du hinzufügen möchtest: ")
        add_name(name_to_add)
    elif choice == '2':
        name_to_remove = input("Gib den Namen ein, den du entfernen möchtest: ")
        remove_name(name_to_remove)
    elif choice == '3':
        display_names()
    elif choice == '4':
        print("Programm beendet.")
        break
    else:
        print("Ungültige Auswahl. Bitte versuche es erneut.")

# Abmelden
con.disconnect()