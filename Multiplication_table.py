"""
Is a mathematical table used to define a multiplication operation for an algebraic system.

"""
import time

used = []
while True:
    number = int(input('Enter the number you want to see its time table: '))
    if number not in used:
        for c in range(1, 11):
            print(f'{number} X {c} = {number * c}')
            time.sleep(0.5)
    used.append(number)
    if used.count(number) > 1:
        print()
        print('Please input anoter number, we already calculated this one.')
        print()
    finalized = str(input('Type "Exit" if you want to leave or enter to input another number: \n')).strip().upper()
    if finalized == "EXIT":
        break





