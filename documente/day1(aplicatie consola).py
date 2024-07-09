def validare_cnp(CNP):
    if len(CNP) != 13:
        print ("Eroare de sintaxa. Prea putine cifre introduse in CNP")
        quit()
    cnpcontrol = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    total = 0
    if CNP[12].isdigit() == False:
        print ("Eroare de sintaxa. Litere introduse in CNP")
        quit()
    for index in range (0, 12, 1):
        if CNP[index].isdigit() == False:
            print ("Eroare de sintaxa. Litere introduse in CNP")
            quit()
        total += int (CNP[index]) * int(cnpcontrol[index])
    total = total % 11
    control = 0
    if (total == 10):
        control = 1
    else: control = total    
    if (int(CNP[12]) != control):
        print("CNP-ul introdus nu este corect.")
        quit()

def validare_litere(nume):
    for index in range(0, len(nume)):
        if nume[index].isdigit() == True:
            print ("Eroare de sintaxa, numere introduse.")
            quit()

def validare_spatii(prenume):
    spatii = 0
    for index in range(0, len(prenume)):
        if prenume[index] == " ":
            spatii += 1
        if prenume[index] == "-":
            spatii += 1
        if (spatii > 2):
            print ("Eroare de sintaxa, prea multe prenume introduse.")
            quit()

def salvare_txt(dictionar):
    with open("date.txt", 'a') as f:  
        for key, value in dictionar.items():  
            f.write('%s:%s\n' % (key, value))
    print("Datele au fost salvate cu succe in format txt!\n")

def salvare_csv(dictionar):            
    with open('date.csv', 'a') as f:
        for key in dictionar.keys():
            f.write("%s,%s\n" % (key,dictionar[key]))
    print("Datele au fost salvare cu succes in format csv!\n")             

while 1>0:
    caz = input ("1. Introduceti un nou cursant \n2. Parasirea programului\nIntroduceti numarul corespunzator actiunii dorite: ")
    match caz:
        case "1":
            nume = input("Va rugam introduceti numele cursantului: ")
            validare_litere(nume)
            prenume = input ("Va rugam introduceti prenumele cursantului: ")
            validare_spatii(prenume)
            validare_litere(prenume)
            CNP = input ("Va rugam introduceti CNP-ul cursantului: ")
            validare_cnp(CNP)
            print ("Datele introduse sunt: \n" "Nume: " + nume + "\n" "Prenume: " + prenume + "\n" "CNP: " + CNP)
            tilda = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            cazz = input ("Doriti salvarea datelor? \n 0 - nu, 1 - Salvare in format txt, 2. Salvare in format CSV\n")
            if (cazz == "1"): 
                dictionar = { 'Nume' : nume, 'Prenume' : prenume, 'CNP' : CNP, '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' : tilda}
                salvare_txt(dictionar) 
            if (cazz == "2"):
                dictionar = { 'Nume' : nume, 'Prenume' : prenume, 'CNP' : CNP} 
                salvare_csv(dictionar)
        case "2":
            quit()