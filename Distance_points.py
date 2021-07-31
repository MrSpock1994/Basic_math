"""
Distance between 2 points.

"""
import math

while True:
    x1 = int(input('Enter the coordinate x1: '))
    y1 = int(input('Enter the coordinate y1: '))
    x2 = int(input('Enter the coordinate x2: '))
    y2 = int(input('Enter the coordinate y1: '))
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(f'For the coordinates {(x1, y1)} and {(x2, y2)}, the distance is: {d:.2f}')
    another = str(input('Do you want to input another coordinate? [Y/N]: ')).upper()
    print()
    while another not in 'YN':
        print('Invalid choice!')
        another = str(input('Do you want to input another coordinate? [Y/N]')).upper()
    if another == 'N':
        print('END!')
        break
