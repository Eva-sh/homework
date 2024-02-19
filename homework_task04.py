from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    # we go through all the elements of the four lists, adding up alternately checking for the condition
    kol = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if (i + j + k + l) == 0:
                        kol += 1
    return kol
