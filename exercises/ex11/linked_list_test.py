"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730465288"


def test_last_empty() -> None:
    """Last of an empty linked list should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """An empty list should return an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, int)


def test_value_at_index_in_list() -> None:
    """An index outside of the limits of the list should return an IndexError."""
    with pytest.raises(IndexError):
        linked_list = Node(1, Node(2, Node(3, None)))
        value_at(linked_list, 3)


def test_value_at_zero_index() -> None:
    """At an index of zero, the data from the head should be returned."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_correct_data() -> None:
    """The data from the Node in the correct index as the argument should be returned."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max_none() -> None:
    """An input of None should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_one_node() -> None:
    """A linked list with a singular Node should return that Node's data."""
    linked_list = Node(1, None)
    assert max(linked_list) == 1


def test_max_increasing() -> None:
    """A linked list with multiple Nodes should return an int that is equal to the data from the Node with the largest data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_max_decreasing() -> None:
    """A linked list with multiple Nodes should return an int that is equal to the data from the Node with the largest data value."""
    linked_list = Node(3, Node(2, Node(1, None)))
    assert max(linked_list) == 3


def test_max_random() -> None:
    """A linked list with multiple Nodes should return an int that is equal to the data from the Node with the largest data value."""
    linked_list = Node(2, Node(3, Node(1, None)))
    assert max(linked_list) == 3


def test_linkify_empty_list() -> None:
    """An empty list should return None."""
    items = []
    assert linkify(items) is None


def test_linkify_single_index() -> None:
    """A list with a single index should return a linked list with a single Node with its data value equivalent to the int in the list."""
    items = [1]
    assert linkify(items) == Node(1, None)


def test_linkify_increasing() -> None:
    """A list with multiple indicies should return a linked list where each Node on that list has a data value that is equal to its corresponding location in the list."""
    items = [1, 2, 3]
    assert linkify(items) == Node(1, Node(2, Node(3, None)))


def test_linkify_random() -> None:
    """A list with multiple indicies should return a linked list where each Node on that list has a data value that is equal to its corresponding location in the list."""
    items = [5, 2, 4, 10]
    assert linkify(items) == Node(5, Node(2, Node(4, Node(10, None))))


def test_scale_one() -> None:
    """A linked list with a single Node should scale that Node's data value by the given factor."""
    linked_list = Node(1, None)
    assert scale(linked_list, 2) == Node(2, None)


def test_scale_none() -> None:
    """An empty linked list should return None."""
    assert scale(None, 2) is None


def test_scale_long() -> None:
    """A linked list with multiple Nodes should have each of its Node's data values multiplied by the factor."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert scale(linked_list, 2) == Node(2, Node(4, Node(6, None)))


def test_scale_linkify() -> None:
    """A linked list of Nodes created by linkify() should have its Node's data values multiplied by the factor."""
    assert scale(linkify([1, 2, 3]), 2) == Node(2, Node(4, Node(6, None)))