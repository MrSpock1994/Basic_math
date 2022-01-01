"""

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""


a = str(2 ** 1000)
list_1 = []
for i in a:
    c = int(i)
    list_1.append(c)
s = sum(list_1)
print(s)