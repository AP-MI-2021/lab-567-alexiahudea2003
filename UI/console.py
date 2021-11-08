from Domain.inventar import to_string, gestionare_obiect, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect, get_by_id
from Logic.functionalitate import mutare_obiect, pret_max, ordonare_obiecte, suma_preturi
from Tests.test_functionalitate import concatenare_string


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutare obiect")
    print("5. Concatenare")
    print("6. Pretul maxim al obiectelor dintr-o locatie")
    print("7. Ordonarea obiectelor crescator dupa pret")
    print("8. Afisarea sumelor preturilor pentru fiecare locatie")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare obiecte")
    print("x. Iesire")

def ui_adaugare_obiect(lista, undo_operations, redo_operations):
    try:
        id = input("Dati id-ul:")
        nume = input("Dati nume:")
        descriere = input("Dati descrierea:")
        pret = float(input("Dati pretul:"))
        locatie = input("Dati locatia:")
        rezultat = adauga_obiect(id, nume, descriere, pret, locatie, lista)
        undo_operations.append([
            lambda: sterge_obiect(id, rezultat),
            lambda: adauga_obiect(id, nume, descriere, pret, locatie, lista)
        ])
        redo_operations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_stergere_obiect(lista, undo_operations, redo_operations):
    try:
        id = input("Dati id-ul obiectului de sters:")
        rezultat = sterge_obiect(id, lista)
        obiect_de_sters = get_by_id(id, lista)
        undo_operations.append([
            lambda: adauga_obiect(
                id,
                get_nume(obiect_de_sters),
                get_descriere(obiect_de_sters),
                get_pret(obiect_de_sters),
                get_locatie(obiect_de_sters),
                rezultat),
            lambda: sterge_obiect(id, lista)
        ])
        redo_operations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_modificare_obiect(lista, undo_operations, redo_operations):
    try:
        id = input("Dati id-ul obiectului de modificat:")
        nume = input("Dati noul nume:")
        descriere = input("Dati noua descriere:")
        pret = float(input("Dati noul pret:"))
        locatie = input("Dati noua locatie:")
        rezultat = modifica_obiect(id, nume, descriere, pret, locatie, lista)
        obiect_vechi = get_by_id(id, lista)
        undo_operations.append([
            lambda: modifica_obiect(
                id,
                get_nume(obiect_vechi),
                get_descriere(obiect_vechi),
                get_pret(obiect_vechi),
                get_locatie(obiect_vechi),
                rezultat),
            lambda: modifica_obiect(id, nume, descriere, pret, locatie, lista)
        ])
        redo_operations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))

def ui_mutare_obiect(lista):
    locatie_noua = input("Dati noua locatie:")
    return mutare_obiect(locatie_noua, lista)

def ui_concatenare(lista):
    valoarea = float(input("Dati valoarea:"))
    string = str(input("Dati string-ul:"))
    return concatenare_string(valoarea, string, lista)

def ui_pret_max(lista):
    rezultat = pret_max(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))

def ui_ordonare_obiecte(lista):
    show_all(ordonare_obiecte(lista))

def ui_suma_preturi(lista):
    rezultat = suma_preturi(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))

def run_menu(lista):
    undo_operations = []
    redo_operations = []
    while True:
        print_menu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista, undo_operations, redo_operations)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista, undo_operations, redo_operations)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista)
        elif optiune == "4":
            lista = ui_mutare_obiect(lista, undo_operations, redo_operations)
        elif optiune == "5":
            lista = ui_concatenare(lista, undo_operations, redo_operations)
        elif optiune == "6":
            lista = ui_pret_max(lista)
        elif optiune == "7":
            lista = ui_ordonare_obiecte(lista, undo_operations, redo_operations)
        elif optiune == "8":
            lista = ui_suma_preturi(lista)
        elif optiune == "u":
            if len(undo_operations) > 0:
                operations = undo_operations.pop()
                redo_operations.append(operations)
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_operations) > 0:
                operations =redo_operations.pop()
                undo_operations.append(operations)
                lista = operations [1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati:")


