"""Utility functions for working with linked lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730465288"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node] 

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last values of a linked list, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None.")
    else:
        n: int = 0
        if head.next is None:
            n = head.data
        else:
            n = last(head.next)
    return n


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the Node stored at the given index on a linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        n: int = 0
        if index == 0:
            n = head.data
        else:
            n = value_at(head.next, index - 1)
    return n


def max(head: Optional[Node]) -> int:
    """Returns the maximum data value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        n: int = head.data
        if head.next is not None:
            if max(head.next) > n:
                n = max(head.next)
    return n


def linkify(items: list[int]) -> Optional[Node]:
    """Returns a linked list of nodes with the same data values as the corresponding index in the input list."""
    n: Optional[Node] = Node(0, None)
    if len(items) == 0:
        n = None
    else: 
        n.data = items[0]
        n.next = linkify(items[1:])
    return n


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales each data point in a linked list by an integer called factor."""
    n: Optional[Node] = Node(0, None)
    if head is None:
        n = None
    else:
        n.data = head.data * factor
        n.next = scale(head.next, factor)
    return n
