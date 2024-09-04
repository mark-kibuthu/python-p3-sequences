#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = [0, 1]

    for i in range(2, length):
        next_value = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_value)

    print(fibonacci_list[:length])

print_fibonacci(9)