"""
Program to inform the user all the divisors of a certain number.

"""

divisors = []

while True:
    num = int(input('What is the number? '))
    for c in range(1,num+1):
        if num % c == 0:
            divisors.append(c)
    print(f'The divisors of {num} are {divisors}.')
    divisors.clear()
    print()
    another = str(input('Do you want to input another number? [Y/N]: ')).upper()
    print()
    while another not in 'YN':
        print('Invalid choice!')
        another = str(input('Do you want to input another number? [Y/N]')).upper()
    if another == 'N':
        print('END!')
        break
