"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
list_1 = []
list_2 = []
c = 1
while c <= 100:
    list_1.append(c**2)
    list_2.append(c)
    c += 1
s = sum(list_1)
s_2 = sum(list_2)
square2 = s_2 ** 2
d = square2 - s
print(d)
