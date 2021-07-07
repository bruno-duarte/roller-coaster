from src.classes.roller_coaster import RollerCoaster
from src.interfaces.menus import *


def main():
    choice = ''
    while choice != '4':
        choice = menu()
        if choice == '1':
            rc = RollerCoaster(12, 1, 4, 1, 10, 3)
            break
        elif choice == '2':
            rc = RollerCoaster(12, 2, 4, 1, 10, 3)
            break
        elif choice == '3':
            rc = RollerCoaster(12, 3, 4, 1, 10, 3)
            break
        elif choice == '4':
            break
        else:
            print('Opção inválida!')
    if choice != '4':
        rc.run()


if __name__ == '__main__':
    main()
