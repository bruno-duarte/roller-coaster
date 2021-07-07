def menu():
    print('---------------------------------------')
    print('ROLLER COASTER')
    print('---------------------------------------')
    print('1. One car')
    print('2. Two cars')
    print('3. Three cars')
    print('4. Exit')
    print()
    choice = input('>>> ')
    print('---------------------------------------')
    return choice


def secondary_menu():
    print('---------------------------------------')
    choice = input('Do you want to run again [Y/n]? ')
    print()
    print('---------------------------------------')
    return choice
