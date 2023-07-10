#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length >= 1:
        fib_list.append(0)
    if length >= 2:
        fib_list.append(1)
    if length > 2:
        a, b = 0, 1
        for _ in range(length - 2):
            a, b = b, a + b
            fib_list.append(b)
    print(fib_list)
    pass