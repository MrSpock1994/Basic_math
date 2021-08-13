"""
Each number in the sequence is the sum of the two numbers that precede it. So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

"""
n = int(input('How many numbers in the sequence do you want to see?: '))
cont = 1
fib = [0, 1]
c = 0
while cont <= (n-2):
    c = (fib[-1] + fib[-2])
    fib.append(c)
    cont = cont + 1
print(fib)
