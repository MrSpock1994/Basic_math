"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def divisors(a):
    n = 1
    global list_1
    list_1 = []
    while n <= a:
        if a % n == 0:
            list_1.append(n)
        n += 1


divisors(600851475143)


def prime(x):
    primes = []
    for i in x:
        p = 0
        if i == 1:
            primes.append(i)
        else:
            for j in range(1, 1+i):
                if i % j == 0:
                    p += 1
            if p == 2:
                primes.append(i)
    largest = max(primes)
    print(primes)
    print(largest)

prime(list_1)





