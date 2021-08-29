"""
A program to estimate the number pi using random numbers between 0 and 1.

"""
import random


def estimate(n):
    point_in_circle = 0
    point_out_circle = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        d = x**2 + y**2
        if d <= 1:
            point_in_circle += 1
        else:
            point_out_circle += 1
    total_points = point_in_circle + point_out_circle
    p = 4 * (point_in_circle / total_points)
    print(p)


points = int(input("Input the number of points: "))
estimate(points)
