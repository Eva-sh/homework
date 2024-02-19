"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = 2  # the index is assigned the value two, since the Fibonacci sequence initially starts with 0 and 1
    new_el = 0  # the new element is assigned 0, since we go from the very beginning of the sequence
    length_data = len(data)  # we assign the variable the length of the array given by the condition
    last_data_el = data[length_data - 1]  # finding the last element of the array

    true_fib_range = [0, 1]  # our original array

    while new_el < last_data_el:  # the loop will do the work until the new element is smaller than the last element
        new_el = true_fib_range[i - 1] + true_fib_range[
            i - 2]  # since in the Fibonacci sequence, the number coming after 0 and 1 is
        # the sum of the previous two, so here we find a new element through the indexes
        true_fib_range.append(
            new_el)  # if the received element has passed the check above, then we add it to our sequence

        i += 1  # and add one to the variable i (index)
    index_for_true_list = len(
        true_fib_range) - length_data  # to cover cases in which the Fibonacci sequence does not start with 0 and 1

    if index_for_true_list < 0:
        return False

    final_list = []  # created an empty array
    for i in range(index_for_true_list, len(true_fib_range)):
        final_list.append(true_fib_range[i])

    return final_list == data  # checking our array with this array by condition

