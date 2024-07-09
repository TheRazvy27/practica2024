#TO DO:
# 1. Numele fisierelor in care sunt salvate datele trebuie sa aiba formatul: Lista_cursanti_AN_LUNA_ZI_ORA_MINUTE.txt/csv
# 2. Stergerea inregistrarilor din cadrul listei de cursanti (adaugarea de index pentru fiecare inregistrare si stergere pe baza de index)
# 2'. Stergerea inregistrarilor pe baza de CNP
# 3. Incarcarea datelor dintr-un fisier de cursanti in cadrul listei cu eliminarea duplicatelor.
from time import strftime
import glob
import csv

def test():
    for filename in glob.glob("C:/Users/c8ilu/documente/*.txt"):
        print(filename)
        open(filename)

#def stergere(id):
#    for filename in glob.glob("C:/Users/c8ilu/documente/*.txt"):
#        with open(filename, mode = "r") as my_file:
#            for lines in my_file:
#                if(f'{id} ') in lines:
#                    print(f'ID-ul {id} a fost sters')
#                    continue
#                my_file.write(lines)

#def stergere_id(id):
#    for filename in glob.glob('documente/*.txt'):
#        with open(filename, mode = "r") as my_file:
#            lines = my_file.readlines()
#        with open(filename, mode = "w") as my_file:
#            for line in lines:
#                if line.rstrip() != id:
#                    my_file.write(line)
#                    print(id, " a fost sters cu succes!")

def stergere_v2(id):
    for filename in glob.glob("C:/Users/c8ilu/documente/*.txt"):
        file = open(filename, "r")
        my_file = file.readlines()
        file.close()
        file = open(filename, "w")
        for line in my_file:
            linie = line.split(' ')
            #print(linie)
            if linie[0] == id:
                print(line.rstrip(), " a fost sters.")
            else:
                file.write(line)



def prelucrare_date_citite(data):
    with open("id.md", "r") as my_file:
        id = my_file.read()
    if len(data) < 3:
        print("Datele introduse pentru cursant sunt incomplete")
        return False
    nume = data[0]
    if len(data) == 3:
        prenume = data[1]
        cnp = data[2]
    if len(data) == 4:
        prenume = data[1] + " " + data[2]
        cnp = data[3]
    with open("id.md", mode = "w") as my_file:
        increment = int(id)
        increment += 1
        my_file.write(f'{increment}')    
    return increment, nume, prenume, cnp


def validare_nume(nume_introdus):
    for index in range(0, len(nume_introdus)):
        if nume_introdus[index].isdigit() == True:
            return False
    return True


def validare_cnp(cnp_introdus):
    # Verificam daca lungimea CNP-ului introdus este de 13 caractere
    if len(cnp_introdus) != 13:
        print("Lungimea CNP-ului nu este corecta.")
        return False
    if not cnp_introdus.isdigit():
        print("CNP-ul trebuie sa contina doar cifre.")
        return False

    # Calculam cifra de control
    constanta_control = "279146358279"
    suma = 0
    for i in range(12):
        suma += int(cnp_introdus[i]) * int(constanta_control[i])
    cifra_control_calculata = suma % 11
    if cifra_control_calculata == 10:
        cifra_control_calculata = 1

    # Verificam cifra_control_calculata vs cifra_control din CNP
    if cifra_control_calculata != int(cnp_introdus[12]):
        print("Cifra de control a CNP-ului nu este corecta.")
        return False
    return True

def salveaza_date(format_fisier):
    global lista_cursanti
    #TODO: Tratarea cazului pentru format_fisier == csv
    if format_fisier == "txt":
        with open(strftime("Lista_cursanti_%Y_%B_%d_%H_%M.txt"), mode = "w") as my_file:
            my_file.write("ID \t Nume \t Prenume \t CNP \n")
        with open(strftime("Lista_cursanti_%Y_%B_%d_%H_%M.txt"), mode = "a") as my_file:
            for cursant in lista_cursanti:
                my_file.write(f'{cursant['id']} \t{cursant['nume']}\t{cursant['prenume']}\t{cursant['cnp']}\n')
        print(f'Fisierul {strftime("Lista_cursanti_%Y_%B_%d_%H_%M.txt")} a fost salvat cu success.')
    if format_fisier == "csv":
        with open(strftime("Lista_cursanti_%Y_%B_%d_%H_%M.csv"), mode = "w", newline = '') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow(['ID', 'Nume',  'Prenume',  'CNP'])
#        with open(strftime("Lista_cursanti_%Y_%B_%d_%H_%M.csv"), mode = 'a', newline = '') as csvfile:
            for cursant in lista_cursanti:
                filewriter.writerow([cursant['id'], cursant['nume'], cursant['prenume'], cursant['cnp']])
        print(f'Fisierul {strftime("Lista_cursanti_%Y_%B_%d_%H_%M.csv")} a fost salvat cu success.')             



if __name__ == "__main__":
    lista_cursanti = []
 #   test()
    while True:
        dict_cursant = dict()
        new_line = input("Introduceti un nou cursant sau introduceti EXIT sau SAVE.")
        if new_line == "EXIT":
            print("Programul se inchide")
            break
        if new_line == "SAVE":
            format_fisier = input("In ce format doriti salvarea datelor? txt/csv?").lower()
            salveaza_date(format_fisier)
            continue
        if new_line == "DELETE":
            delete = input("Introduceti ID-ul pe care doriti sa il stergeti: ")
            stergere_v2(delete)
            continue
        date_cursant = new_line.split()
        rezultat = prelucrare_date_citite(date_cursant)
        if not rezultat:
            continue
        id = rezultat[0]
        nume = rezultat[1]
        prenume = rezultat[2]
        cnp = rezultat[3]
        if not validare_cnp(cnp):
            continue
        if not validare_nume(nume):
            print("Numele introdus nu este valid.")
        if not validare_nume(prenume):
            print("Prenumele introdus nu este valid.")
        # dict_cursant['nume'] = nume
        # dict_cursant['prenume'] = prenume
        # dict_cursant['cnp'] = cnp
        dict_cursant = {"id": id, "nume": nume, "prenume": prenume, "cnp": cnp}
        lista_cursanti.append(dict_cursant)
        print(lista_cursanti)