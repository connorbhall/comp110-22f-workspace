"""Utilizing the List function to get a better understanding of lists in Python."""

__author__ = 730465288

from re import I


def all(integers: list[int], number: int) -> bool:
    "A function that checks each index of a list to see if they match the given int."
    i: int = 1
    check: bool = False

    while i < len(integers):
        if integers[i] == number:
            check = True
        if integers[i] != number:
            check = False
        i += 1
    return print(check)


def max(input: list[int]) -> int:
    """Returns an int that is the largest number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
   
    i: int = 1
    maxint: int = input[0]
    
    while i < len(input):
        if maxint > input[i]:
            i += 1
        elif maxint < input[i]: 
            maxint = input[i]
            i += 1
        
    return maxint 


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are identical."""
    if list1 == list2:
        return True
    else:
        return False