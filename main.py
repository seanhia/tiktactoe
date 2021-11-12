def rules():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" 1. You are player 'X' ")
    print(" 2. Choose a position 1-9")
    print('     | 1 | 2 | 3 |')
    print('     |---|---|---|')
    print('     | 4 | 5 | 6 |')
    print('     |---|---|---|')
    print('     | 7 | 8 | 9 |')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def grid():
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')


def pos1():
    print('| X |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')


def pos2():
    print('|   | X |   |')
    print('|---|---|---|')
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')


def pos3():
    print('|   |   | X |')
    print('|---|---|---|')
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')


def pos4():
    print('|   |   |   |')
    print('|---|---|---|')
    print('| X |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')


def pos5():
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   | X |   |')
    print('|---|---|---|')
    print('|   |   |   |')


def pos6():
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   | X |')
    print('|---|---|---|')
    print('|   |   |   |')


def pos7():
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')
    print('|---|---|---|')
    print('| X |   |   |')


def pos8():
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   | X |   |')


def pos9():
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   |   |')
    print('|---|---|---|')
    print('|   |   | X |')


if __name__ == '__main__':
    on = 1
    on2 = 1
    on3 = 1
    while on == 1:
        start = input("DO YOU WANT TO PLAY TIK-TAC-TOE? (type 'yes' or 'no') \n")
        if start == "yes":
            rules()
            on = 0
        elif start == "no":
            print("Why are you here then...")
            on = 0
        else:
            print("(type 'yes' or 'no')")
        ready = input("ARE YOU READY? (type 'yes' or 'no') \n")
        while on2 == 1:
            if ready == "yes":
                position = input("Choose a position 1-9 \n")
                on2 = 0
                while on3 == 1:
                    if position == "1":
                        pos1()
                        on3 = 0
                    elif position == "2":
                        pos2()
                        on3 = 0
                    elif position == "3":
                        pos3()
                        on3 = 0
                    elif position == "4":
                        pos4()
                        on3 = 0
                    elif position == "5":
                        pos5()
                        on3 = 0
                    elif position == "6":
                        pos6()
                        on3 = 0
                    elif position == "7":
                        pos7()
                        on3 = 0
                    elif position == "8":
                        pos8()
                        on3 = 0
                    elif position == "9":
                        pos9()
                        on3 = 0
                    else:
                        print("Choose a position 1-9")
            elif ready == "no":
                print("Why are you here then...")
                on2 = 0
            else:
                print("(type 'yes' or 'no')")

