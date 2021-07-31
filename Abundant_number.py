"""
Program to find out, if the given number is abundant.

Note: In number theory, an abundant number or excessive number is a
number for which the sum of its proper divisors is greater than the number itself.

"""

while True:
    s = 0
    num = int(input('Enter the number: '))
    for c in range(1, num):
        if num % c == 0:
            s += c
    if s > num:
        print(f'{num} is an abundant number, and the sum of its divisors is {s}.')
        print()
    else:
        print(f'{num} is not an abundant number.')
        print()
    another = str(input('Do you want to input another number? [Y/N]: ')).upper()
    print()
    while another not in 'YN':
        print('Invalid choice!')
        another = str(input('Do you want to input another number? [Y/N]')).upper()
    if another == 'N':
        print('END!')
        break

