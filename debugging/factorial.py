#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to prevent infinite loop
    return result

f = factorial(int(sys.argv[1]))
print(f)
