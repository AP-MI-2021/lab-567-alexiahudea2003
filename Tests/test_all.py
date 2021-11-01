from Tests.test_CRUD import test_adauga_obiect, test_sterge_obiect, test_modifica_obiect
from Tests.test_Domain import test_obiect
from Tests.test_functionalitate import test_mutare_obiect, test_concatenare


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_sterge_obiect()
    test_modifica_obiect()
    test_mutare_obiect()
    test_concatenare()