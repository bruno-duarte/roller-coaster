from src.classes.roller_coaster import RollerCoaster
from src.utils.menus import *
from src.utils.messages import show_message, INVALID_OPTION
from src.utils.constants import (
    NONE,
    ONE_CAR,
    TWO_CARS,
    THREE_CARS,
    EXIT
)


def main():
    choice = NONE
    while choice != EXIT:
        choice = menu()
        if choice == ONE_CAR:
            rc = RollerCoaster(52, 1, 4, 1, 10, 3)
            break
        elif choice == TWO_CARS:
            rc = RollerCoaster(92, 2, 4, 1, 10, 3)
            break
        elif choice == THREE_CARS:
            rc = RollerCoaster(148, 3, 4, 1, 10, 3)
            break
        elif choice == EXIT:
            break
        else:
            show_message(INVALID_OPTION)
    if choice != EXIT:
        rc.run()


if __name__ == '__main__':
    main()
