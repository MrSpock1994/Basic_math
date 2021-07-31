"""
Program to inform the user if a certain number is a prime or not.

"""


def prime(n):
    p = 0
    for c in range(1, n+1):
        if n % c == 0:
            p += 1
    if p == 2:
         print(f'{n} is a prime number!')
    if p > 2:
        print(f'{n} is not a prime number!')


num = int(input('Enter the number: '))
prime(num)
