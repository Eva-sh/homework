from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    podmas = []
    for i in range(len(nums)):
        podmas = nums[i:i + k]  # array containing elements from i to i+k
        if sum(podmas) > max_sum:  # checking the sum of the current subarray with the maximum amount found
            max_sum = sum(podmas)
    return max_sum
