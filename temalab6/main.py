from Logic.CRUD import adauga_obiect
from Tests.test_all import run_all_tests
from UI.console import run_menu

def main():
    run_all_tests()
    lista = []
    lista = adauga_obiect("1","tabla","alba",300,"s204",lista)
    lista = adauga_obiect("2","birou","lemn",500,"s203",lista)
    run_menu(lista)
main()