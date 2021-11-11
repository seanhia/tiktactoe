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


if __name__ == '__main__':
    on = 1
    on2 = 1
    while on == 1:
        start = input("DO YOU WANT TO PLAY TIK-TAC-TOE? (type 'yes' or 'no') \n")
        if start == "yes":
            rules()
            ready = input("ARE YOU READY? (type 'yes' or 'no') \n")
            while on2 == 1:
                if ready == "yes":
                    grid()
                    position = input("Choose a position 1-9 \n")

                if ready == "no":
                    print("Why are you here then...")
                    on2 = 0
                else:
                    print("(type 'yes' or 'no')")
        if start == "no":
            print("Why are you here then...")
            on = 0
        else:
            print("(type 'yes' or 'no')")

