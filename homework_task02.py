"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    true_fib_rage = [0, 1]
    for i in range(2, len(data)):
        new_el = true_fib_rage[i - 1] + true_fib_rage[i - 2]
        true_fib_rage.append(new_el)
    return true_fib_rage == data


# data_to_process = [0, 1, 1, 2, 3, 5]
# print(check_fibonacci(data_to_process))
