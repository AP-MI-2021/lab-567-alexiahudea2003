from Domain.inventar import to_string
from Logic.CRUD import adauga_obiect, modifica_obiect, sterge_obiect
from UI.console import show_all


def command_line_console(lista):
    while True:
        try:
            print("comanda help - pentru ajutor")
            comanda = input("Dati comanda")
            if comanda == "help":
                print("!comenzile se separa prin punct si virgula!")
                print("add- pentru adaugare obiect")
                print("update- pentru a modifica obiect")
                print("delete- pentru a sterge obiect")
                print("showall- pentru afisarea obiectelor")
                print("stop- pentru a iesi")
            elif comanda == "stop":
                break
            else:
                executa = comanda.split(";")
                for i in range(len(executa)):
                    comanda_separata = executa[i].split(",")
                    if comanda_separata[0] == "add":
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        descriere = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        locatie = comanda_separata[5]
                        lista = adauga_obiect(id, nume, descriere, pret, locatie, lista)
                    elif comanda_separata[0] == "delete":
                        id = comanda_separata[1]
                        lista = sterge_obiect(id, lista)
                        print("s-a sters un obiect")
                    elif comanda_separata[0] == "update":
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        descriere = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        locatie = comanda_separata[5]
                        lista - modifica_obiect(id, nume, descriere, pret, locatie, lista)
                        print("au fost modificate obiecte")
                    elif comanda_separata[0] == "showall":
                        show_all(lista)
                    else:
                        print("nu exista comanda")
        except ValueError as ve:
            print("Eroare: {}".format(ve))