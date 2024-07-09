import tkinter as tk
import csv

def validare_cnp(CNP):
    if len(CNP) != 13:
        eroare("Prea putine cifre introduse in CNP!") 
    cnpcontrol = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    total = 0
    if CNP[12].isdigit() == False:
        eroare("Litere detectate in CNP!")
    for index in range (0, 12, 1):
        if CNP[index].isdigit() == False:
            eroare("Litere detectate in CNP!")
        total += int (CNP[index]) * int(cnpcontrol[index])
    total = total % 11
    control = 0
    if (total == 10):
        control = 1
    else: control = total    
    if (int(CNP[12]) != control):
        eroare("CNP-ul introdus nu este corect!")

def validare_litere(nume):
    for index in range(0, len(nume)):
        if nume[index].isdigit() == True:
            eroare("Numere detectate in numele de famiilie/prenume!")       

def validare_spatii(prenume):
    spatii = 0
    for index in range(0, len(prenume)):
        if prenume[index] == " ":
            spatii += 1
        if prenume[index] == "-":
            spatii += 1   
    if (spatii > 2):
        eroare("Prea multe spatii detectate in prenumele introdus!")   

def salvare_txt():
    dictionar = valideaza()
    dictionar['~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'] = tilda
    with open("date.txt", 'a') as f:  
        for key, value in dictionar.items():  
            f.write('%s:%s\n' % (key, value))
    succes("Datele au fost salvate cu succes in format txt!")
    

def salvare_csv():
    dictionar = valideaza()
    with open('date.csv', 'a') as f:
        for key in dictionar.keys():
            f.write("%s,%s\n" % (key,dictionar[key]))
    succes("Datele au fost salvate cu succes in format csv!")
    

def quit():
    window.destroy()

def succes(mesaj):
    textbox.delete(0, 99)
    textbox2.delete(0, 99)
    textbox3.delete(0, 99)
    succes = tk.Label(text = mesaj, fg = "green")
    succes.pack()
    eroare(" ")

def eroare(mesaj):
    eroaret = tk.Label(text = mesaj, fg = "red")
    eroaret.pack()
    succes(" ")

def valideaza():
    nume = textbox.get() 
    validare_litere(nume)
    prenume = textbox2.get()
    validare_litere(prenume)
    validare_spatii(prenume)
    CNP = textbox3.get()
    validare_cnp(CNP)
    dictionar = { 'Nume' : nume, 'Prenume' : prenume, 'CNP' : CNP} 
    return dictionar          
                              
tilda = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
window = tk.Tk()
window.title("Cursant nou")
window.geometry("500x300")
numet = tk.Label(text = "Nume")
prenumet = tk.Label(text = "Prenume")
CNPt = tk.Label (text = "CNP")
textbox = tk.Entry(window, width = 20)
textbox2 = tk.Entry(window, width = 20)
textbox3 = tk.Entry(window, width = 20)
Button = tk.Button (window, text = "Salveaza datele in format csv", command = salvare_csv)
Button2 = tk.Button (window, text = "Salveaza datele in format txt", command = salvare_txt)
qbuton = tk.Button (window, text = "Paraseste programul", command = quit)

numet.pack()
textbox.pack()

prenumet.pack()
textbox2.pack()

CNPt.pack()
textbox3.pack()

Button.pack()
Button2.pack()
qbuton.pack()

window.mainloop()