"""Understanding the test function that is available through Pylance."""

__author__ = 730465288


def only_evens(list_1: list[int]) -> list[int]:
    """Returns a list of only even integers from a larger list."""
    i: int = 0
    list_2: list[int] = []
    while i < len(list_1):
        if (list_1[i] % 2) == 0:
            list_2.append(list_1[i])
            i += 1
        else: 
            i += 1
    return list_2


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns one list with components from list one and two."""
    list_total: list[int] = []
    for ints_1 in list_1:
        list_total.append(ints_1)
    for ints_2 in list_2:
        list_total.append(ints_2)
    return list_total


def sub(a_list: list[int], index_1: int, index_2: int) -> list[int]:
    """Returns a list comprised of a range of indexes from the initial list."""
    b_list: list[int] = []
    if index_1 < 0:
        index_1 = 0
    if index_2 > len(a_list):
        index_2 = len(a_list)
    
    while index_1 < index_2:
        b_list.append(a_list[index_1])
        index_1 += 1
    return b_list