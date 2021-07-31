"""
Simple math quiz

"""
import random
import time

while True:
    print('*' * 30)
    print('MATH QUIZ'.center(30))
    print('*' * 30)
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Integer Division')
    print('5. Exit')
    print('-' * 30)
    p = int(input('Enter your choice: '))
    options = [1, 2, 3, 4, 5]
    while p not in options[:]:
        print('Invalid choice!!')
        p = int(input('Enter your choice: '))
    if p == 1:
        c = 1
        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            s = x + y
            print(f'{c}° Question!')
            print(f'{x} + {y} is equal to....')
            r = int(input('Answer: '))
            print()
            time.sleep(1)
            if r == s:
                print('RIGHT!!')
                print()
                c += 1
                time.sleep(1)
            else:
                print('WRONG ANSWER!')
                print('Wait a few seconds, we will take you back to the menu...')
                time.sleep(2)
                print('*' * 52)
                break
    if p == 2:
        c = 1
        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            s = x - y
            print(f'{c}° Question!')
            print(f'{x} - {y} is equal to....')
            r = int(input('Answer: '))
            print()
            time.sleep(1)
            if r == s:
                print('RIGHT!!')
                print()
                c += 1
                time.sleep(1)
            else:
                print('WRONG ANSWER!')
                print('Wait a few seconds, we will take you back to the menu...')
                time.sleep(2)
                print('*' * 52)
                break
    if p == 3:
        c = 1
        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            s = x * y
            print(f'{c}° Question!')
            print(f'{x} * {y} is equal to....')
            r = int(input('Answer: '))
            print()
            time.sleep(1)
            if r == s:
                print('RIGHT!!')
                print()
                c += 1
                time.sleep(1)
            else:
                print('WRONG ANSWER!')
                print('Wait a few seconds, we will take you back to the menu...')
                time.sleep(2)
                print('*' * 52)
                break
    if p == 4:
        c = 1
        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            s = x / y
            print(f'{c}° Question!')
            print(f'{x} divided by {y} is equal to....')
            r = int(input('Answer: '))
            print()
            time.sleep(1)
            if r == s:
                print('RIGHT!!')
                print()
                c += 1
                time.sleep(1)
            else:
                print('WRONG ANSWER!')
                print('Wait a few seconds, we will take you back to the menu...')
                time.sleep(2)
                print('*' * 52)
                break
    if p == 5:
        print('END!!')
        break
