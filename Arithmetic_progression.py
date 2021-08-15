"""
An arithmetic progression or arithmetic sequence is a sequence of numbers such
that the difference between the consecutive terms is constant.
an = a1 + (n-1)*d

"""

while True:
    print('*' * 40)
    print('What do you want to do?')
    print('1 - any term of the sequence.')
    print('2 - the first term of the sequence.')
    print('3 - the commom difference of the sequence.')
    print('4 - the amount of terms of the sequence.')
    print('*' * 40)
    ch = int(input('Enter with your choice: '))
    answers = [1, 2, 3, 4]
    if ch == 1:
        print('Now you have to input the initial number of the sequence,'
              'the number of terms and the common difference.')
        print()
        a1 = int(input('What is the initial number?: '))
        n = int(input('How many terms?: '))
        d = int(input('What is the common difference?: '))
        an = a1 + (n - 1)*d
        print(f'The number you are looking for is: {an}')
        print()
        print('The sum of the members for this sequence is:')
        s = (n * (a1 + an)) / 2
        print(s)
        print()
        another = str(input('Do you want to do choose another option? [Y/N]: ')).upper().strip()
        if another == "N":
            break
    if ch == 2:
        print('Now you have to input the final number of the sequence,'
              'the number of terms and the common difference.')
        print()
        an = int(input('What is the final number?: '))
        n = int(input('How many terms?: '))
        d = int(input('What is the common difference?: '))
        a1 = an - (n - 1)*d
        print(f'The number you are looking for is: {a1}')
        print()
        print('The sum of the members for this sequence is:')
        s = (n*(a1+an)) / 2
        print(s)
        print()
        another = str(input('Do you want to do choose another option? [Y/N]: ')).upper().strip()
        if another == "N":
            break
    if ch == 3:
        print('Now you have to input the initial number of the sequence,'
              'the number of terms and the final number of the sequence.')
        print()
        a1 = int(input('What is the initial number?: '))
        n = int(input('How many terms?: '))
        an = int(input('What is the final number?: '))
        d = ((an - a1) / (n - 1))
        print(f'The number you are looking for is: {d}')
        print()
        print('The sum of the members for this sequence is:')
        s = (n * (a1 + an)) / 2
        print(s)
        print()
        another = str(input('Do you want to do choose another option? [Y/N]: ')).upper().strip()
        if another == "N":
            break
    if ch == 4:
        print('Now you have to input the initial number of the sequence,'
              'the common difference and the final number of the sequence.')
        print()
        a1 = int(input('What is the initial number?: '))
        d = int(input('what is the common difference?: '))
        an = int(input('What is the final number?: '))
        n = ((an - a1)/d) + 1
        print(f'The number you are looking for is: {n}')
        print()
        print('The sum of the members for this sequence is:')
        s = (n * (a1 + an)) / 2
        print(s)
        print()
        another = str(input('Do you want to do choose another option? [Y/N]: ')).upper().strip()
        if another == "N":
            break
    if ch not in answers:
        print('INVALID OPTION, TRY AGAIN.')




