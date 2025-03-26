import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QComboBox
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore
from PyQt5 import QtGui


class MyWindow(QMainWindow):
    def __init__(self):
     super(MyWindow,self).__init__()
     self.initUI()


    def initUI(self):
        self.setWindowTitle("Passwort Manager") #Titel der App
        self.setGeometry(100,100,400,300)
        self.setWindowIcon(QtGui.QIcon('images.png'))
        # X,Y höhe, breite der Anwendung

        #Definiert hier das Layout, das die Buttons Zentral in der mitte sein sollen
        self.central_widget=QWidget()
        self.layout = QVBoxLayout()

        self.label =QLabel(self)


        #Definiert die einzelnen Buttons, gibt Ihnen text und weißt ihnen ihre Funktion zu
        self.loginBtn=QPushButton(self)  #Druckt sich selbst quasi
        self.loginBtn.setText("Login")      #Definiert den Visuell Name
        self.loginBtn.clicked.connect(self.login)   #bedient die funktion, bzw "Connected" sie

        self.createNewAccountBtn = QPushButton(self)
        self.createNewAccountBtn.setText("Neuen Benutzer erstellen")
        self.createNewAccountBtn.clicked.connect(self.createUser)

        self.beendenBtn = QPushButton(self)
        self.beendenBtn.setText("Beenden")
        #beendenBtn.move(50,60) braucht man nicht, wenn man das Layout hat und AdjustSize
        self.beendenBtn.clicked.connect(self.beenden)

        #Searchbar
        self.searchbar=QLineEdit()


        #Fügt die Buttons in das Layout ein und sorgt für bessere Übersicht
        self.layout.addWidget(self.label)

        self.layout.addWidget(self.loginBtn)
        self.layout.addWidget(self.createNewAccountBtn)
        self.layout.addWidget(self.beendenBtn)


        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.update()

    def update(self):
        self.label.adjustSize()







    def button_clicked(self):
        self.label.setText("Erfolgreich gedrückt")
        self.update()
        self.label.adjustSize()



    def beenden(self):

        QApplication.quit()





    def login(self):

        #Definiert im Detail, das Pop-Up nach dem Klick auf "Login" im Main Window
        msg = QDialog()
        msg.setWindowTitle("Login")
        msg.setWindowIcon(QtGui.QIcon('images.png'))
        msg_layout = QVBoxLayout()

        #Setzt Text in MSG Fenster
        label = QLabel("Bitte gib deinen Username und dein Passwort ein.")
        msg_layout.addWidget(label)


        #Definiert die einzelnen Widgets

        #Inputfelder
        username_input = QLineEdit()
        username_input.setPlaceholderText("Username")


        password_input= QLineEdit()
        password_input.setPlaceholderText("Password")
        password_input.setEchoMode(QLineEdit.Password)


        #Buttons
        ok_btn = QPushButton("Ok")
        abort_btn = QPushButton("Abbrechen")

        #Fügt oben definierte Widgets ein, von oben nach unten

        #Fügt Eingabefelder ein
        msg_layout.addWidget(username_input)

        pass1_layout = self.create_password_field(password_input)
        msg_layout.addLayout(pass1_layout)

        #Fügt buttons ein
        msg_layout.addWidget(ok_btn)
        msg_layout.addWidget(abort_btn)


        ok_btn.clicked.connect(lambda: self.process_login(username_input.text(),password_input.text(),msg))
        abort_btn.clicked.connect(msg.reject)

        msg.setLayout(msg_layout)
        #Execute of msg
        msg.exec_()


    def process_login(self,username,password,dialog):
        if username == "admin" and password =="1234":
            dialog.accept()
            self.open_password_manager()
        else:

            QMessageBox.warning(self,"Fehler","Falscher Benutzername und Passwort!")

    def open_password_manager(self):
        self.pwMgn = PasswordManagerGUI()
        self.pwMgn.show()
        self.close()

    def createUser(self):
            # Definiert im Detail, das Pop-Up nach dem Klick auf "Login" im Main Window
            msg = QDialog()
            msg.setWindowTitle("Benutzer erstellen")
            msg.setWindowIcon(QtGui.QIcon('images.png'))
            msg_layout = QVBoxLayout()

            # Setzt Text in MSG Fenster
            label = QLabel("Willkommen im Passwort Manager, bitte gib uns folgende Daten an:")
            msg_layout.addWidget(label)

            # Definiert die einzelnen Widgets

            # Inputfelder
            username_input = QLineEdit()
            username_input.setPlaceholderText("Username")

            first_name = QLineEdit()
            first_name.setPlaceholderText("Vorname")
            second_name = QLineEdit()
            second_name.setPlaceholderText("Nachname")

            email_input = QLineEdit()
            email_input.setPlaceholderText("E-Mail")

            gender_selection = QComboBox()
            gender_selection.addItem("Bitte Geschlecht wählen...")
            gender_selection.addItems(["Mann","Frau","Trans","Non-Binary"])
            gender_selection.setCurrentIndex(0)

            birth_layout = QHBoxLayout()
            day_input = QComboBox()
            month_input = QComboBox()
            year_input = QComboBox()

            day_input.addItems([str(i) for i in range(1,32)])
            month_input.addItems(["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"])
            year_input.addItems([str(i) for i in range(1920,2025)])

            password_input = QLineEdit()
            password_input.setPlaceholderText("Password")
            password_input.setEchoMode(QLineEdit.Password)

            password_input2 = QLineEdit()
            password_input2.setPlaceholderText("Wiederholte Passwort eingabe")
            password_input2.setEchoMode(QLineEdit.Password)

            admin_check = QCheckBox()
            admin_check.setText("Ist User ein Admin?")


            # Buttons
            create_btn = QPushButton("Erstellen")
            abort_btn = QPushButton("Abbrechen")

            # Fügt oben definierte Widgets ein, von oben nach unten

            # Fügt Eingabefelder ein
            msg_layout.addWidget(gender_selection)
            msg_layout.addWidget(first_name)
            msg_layout.addWidget(second_name)

            #Erstellt eigenes Layout für die Birth angaben
            birth_layout.addWidget(day_input)
            birth_layout.addWidget(month_input)
            birth_layout.addWidget(year_input)
            #Fügt die dem großen MSG layout hinzu
            msg_layout.addLayout(birth_layout)

            msg_layout.addWidget(email_input)
            msg_layout.addWidget(username_input)


            pass1_layout = self.create_password_field(password_input)
            msg_layout.addLayout(pass1_layout)
            pass2_layout = self.create_password_field(password_input2)
            msg_layout.addLayout(pass2_layout)


            msg_layout.addWidget(admin_check)

            # Fügt buttons ein
            msg_layout.addWidget(create_btn)
            msg_layout.addWidget(abort_btn)

            #create_btn.clicked.connect(lambda: self.process_login(username_input.text(), password_input.text(), msg))
            abort_btn.clicked.connect(msg.reject)

            msg.setLayout(msg_layout)
            # Execute of msg
            msg.exec_()

    def create_password_field(self,password_field):

        layout = QHBoxLayout()

        toggle_btn = QPushButton()
        toggle_btn.setIcon(QIcon('eyes_closed.png'))
        toggle_btn.setCheckable(True)
        toggle_btn.setFixedSize(30,30)
        toggle_btn.clicked.connect(lambda:self.toggle_password_visibility(password_field,toggle_btn))

        layout.addWidget(password_field)
        layout.addWidget(toggle_btn)

        return layout

    def toggle_password_visibility(self,password_field,button):

        if button.isChecked():
            password_field.setEchoMode(QLineEdit.Normal)
            button.setIcon(QIcon('eyes_open.png'))
        else:
            password_field.setEchoMode(QLineEdit.Password)
            button.setIcon(QIcon('eyes_closed.png'))












#Initialisiert nach dem Login das neue MainWindow - also den PasswordManager
class PasswordManagerGUI(QMainWindow):
    def __init__(self):
     super(PasswordManagerGUI,self).__init__()
     self.setWindowTitle("Passwort Manager")  # Titel der App
     self.setGeometry(500, 500, 400, 300)
     self.setWindowIcon(QtGui.QIcon('images.png'))
     self.initUI()


#Definiert hier wieder das neue Design und fügt aussehen hinzu
    def initUI(self):

        self.centralWidget = QWidget()
        self.layout = QVBoxLayout()


        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        searchbar = QLineEdit()
        searchbar.setPlaceholderText("Suche in mir...")

        self.layout.addWidget(searchbar)




        self.layout2 = QVBoxLayout()
        self.test = QGroupBox("Tresorübersicht",self)
        self.test.setFixedHeight(200)
        self.test.setLayout(self.layout2)
        self.layout.addWidget(self.test)



        label = QLabel(self)
        self.layout.addWidget(label)
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)


        #Anordnung anpassen

        meinTresor = QLabel()
        meinTresor.setText("Mein Tresor")


        firmenTresor = QLabel()
        firmenTresor.setText("Firmen Tresor")


        scrollbar = QScrollBar()

        

        logoutBtn = QPushButton()
        logoutBtn.setText("Logout")
        logoutBtn.clicked.connect(self.logout)



        self.layout2.addWidget(meinTresor)
        self.layout2.addWidget(firmenTresor)
        self.layout2.addWidget(scrollbar)


        self.layout.addWidget(logoutBtn)


    def logout(self):



         logoutAlarm = QMessageBox.warning(self, "Sie werden ausgeloggt...", "Auf wiedersehen!",QMessageBox.Ok | QMessageBox.Cancel)

         if logoutAlarm == QMessageBox.Ok:
            self.close()
            self.main_window = MyWindow()
            self.main_window.show()


#führt die Main aus
"""
if __name__ == "__main__":

        app = QApplication(sys.argv)
        window = MyWindow()
        window.show()
        sys.exit(app.exec())

"""


def window():
        app =QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())


