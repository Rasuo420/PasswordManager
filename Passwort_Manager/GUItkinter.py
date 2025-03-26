from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def mainWindow():
root = Tk()
root.title("Password Manager")
root.iconbitmap(r'C:\Users\luca.schwalm\PycharmProjects\PasswordManager\Passwort_Manager\images.ico')

frame = ttk.Frame(root)
frame.grid(row = 0, coloumn = 0,padx = 10, paxy = 10)


root.mainloop()

