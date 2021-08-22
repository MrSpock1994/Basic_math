"""
In mathematics, a geometric progression, also known as a geometric sequence,
is a sequence of non-zero numbers where each term after the first is found by multiplying the previous one by a fixed,
non-zero number called the common ratio
"""
import time
print('Welcome to the GP calculator, you will find more information about the functionality in the menu below.')
while True:
    print('*' * 40)
    print('******************MENU******************')
    print('*' * 40)
    print('What do you want to do?')
    print('1 - Any term of the sequence.')
    print('2 - First term of the sequence')
    print('3 - The common ratio.')
    print('4 - END PROGRAM')
    print('0 - HELP')
    ch = int(input('Enter with your choice: '))
    answers = [0, 1, 2, 3, 4]
    if ch == 0:
        print('*******This is a brief explanation about the functionality******')
        print()
        print('If you choose "1" in the Menu above'
              ' it means we will calculated the nth term of the sequence,\nin order to do so, we require'
              ' the first term, the common ratio and the number of terms.')
        print()
        print('If you choose "2" in the Menu above'
              ' it means we will calculated the first term of the sequence,\nin order to do so, we require'
              ' the last term, the common ratio and the number of terms.')
        print()
        print('If you choose "3" in the Menu above'
              ' it means we will calculated the common ratio of the sequence,\nin order to do so, we require'
              ' the first term, the last term and the number of terms.')
        print()
        ex = int(input('Do you want to exit the program or return to the menu?\nExit = 0\nReturn to Menu = 1\nchoice: '))
        if ex == 0:
            break
        if ex == 1:
            print('We are taking you back to the menu, wait a few seconds...')
        time.sleep(2)
    if ch == 1:
        a1 = float(input('Enter with the first term: '))
        r = float(input('Enter with the common ratio: '))
        n = float(input('Enter with the amount of terms: '))
        an = a1 * (r**(n-1))
        print()
        print('Calculating....')
        time.sleep(1.5)
        print(f'The number you are looking for is {an}')
        print()
        another = str(input('Do you want to do choose another option? [Y/N]: ')).upper().strip()
        if another == "N":
            break
    if ch == 2:
        an = float(input('Enter with the last term: '))
        r = float(input('Enter with the common ratio: '))
        n = float(input('Enter with the amount of terms: '))
        a1 = an / (r**(n-1))
        print()
        print('Calculating....')
        time.sleep(1.5)
        print(f'The number you are looking for is {a1}')
        print()
        another = str(input('Do you want to do choose another option? [Y/N]: ')).upper().strip()
        if another == "N":
            break
    if ch == 3:
        a1 = float(input('Enter with the first term: '))
        an = float(input('Enter with the last term: '))
        n = float(input('Enter with the amount of terms: '))
        r = (an/a1)**(1/(n-1))
        print()
        print('Calculating....')
        time.sleep(1.5)
        print(f'The number you are looking for is {r}')
        print()
        another = str(input('Do you want to do choose another option? [Y/N]: ')).upper().strip()
        if another == "N":
            break
    if ch == 4:
        print('Thanks, see you later!')
        break




