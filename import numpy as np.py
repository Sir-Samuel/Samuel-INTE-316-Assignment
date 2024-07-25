import numpy as np

def f(x):
    return x**2

x = 2
h = 1e-6
derivative = (f(x + h) - f(x)) / h
print(derivative)
