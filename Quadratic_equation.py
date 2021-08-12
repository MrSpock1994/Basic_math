"""
Program to solve a quadratic equation

A quadratic equation is an equation of the second degree, meaning it contains at least one term that is squared.
The standard form is ax² + bx + c = 0 with a, b and c being constants, or numerical coefficients,
and x being an unknown variable.

"""
import time
import math


print('*' * 20)
print('f(x) = ax² + bx + c')
print('*' * 20)
while True:
    a = int(input('Enter with the numerical coefficient "a": '))
    b = int(input('Enter with the numerical coefficient "b": '))
    c = int(input('Enter with the numerical coefficient "c": '))
    d = b**2 - 4*a*c
    try:
        d1 = math.sqrt(d)
    except:
        print('The equation does not have real number solution!!')
        break
    vx = -(b/(2*a))
    vy = -(d/(4*a))
    if d == 0:
        print('The equation has two equal solutions:')
        time.sleep(2)
        s = -b/(2*a)
        print(f'{s:.2f}')
    if d > 0:
        print('The equation has two different solutions:')
        time.sleep(2)
        s1 = (-b + d1) / (2*a)
        s2 = (-b - d1) / (2*a)
        print(f'{s1:.2f} and {s2:.2f}')
    if a > 0:
        print('This equation has a minimum value:')
        print(f'The coordinates of the vertex are: {vx:.2f}, {vy:.2f}')
    if a < 0:
        print('This equation has a maximum value:')
        print(f'The coordinates of the vertex are: {vx:.2f}, {vy:.2f}')
    print('*' * 45)
    another = str(input('Do you want to input another coefficient? [Y/N]: ')).upper()
    print()
    while another not in 'YN':
        print('Invalid choice!')
        another = str(input('Do you want to input another coefficient? [Y/N]')).upper()
    if another == 'N':
        print('END!')
        break


