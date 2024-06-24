"""
Find such x, so that x^2+sqrt(x)=C with an accuracy of at least 6 decimal points.

Input: One real number C

Output: Print the desired root x with at least 6 digits after the decimal point.

solve in python in as little code as possible
"""

from math import sqrt


def f(x, C):
    return x**2 + sqrt(x) - C


def df(x):
    return 2 * x + 0.5 / sqrt(x)


def newton_raphson(x, C, epsilon=1e-6):
    while abs(f(x, C)) > epsilon:
        x = x - f(x, C) / df(x)
    return round(x, 6)


C = float(input("Enter the value of C: "))
x = 1
print("The root is:", newton_raphson(x, C))
