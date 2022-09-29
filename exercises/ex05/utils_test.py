"""Tests for the ex05 functions."""


__author__ = 730465288


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests that only_even returns an empty list when given an empty list."""
    list_1: list[int] = []
    assert only_evens(list_1) == []


def test_only_evens_all_odds() -> None:
    """Tests that only_even returns an empty list when given a list of all odd ints."""
    assert only_evens([1, 5, 3]) == []


def test_only_evens_all_fours() -> None:
    """Tests that only_even returns the initial list when given a list of all evens."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_only_evens() -> None:
    """Tests that only_even returns a list of only even numbers from the given list of random integers."""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_concat_empty() -> None:
    """Tests that concat returns an empty list when given two empty lists."""
    assert concat([], []) == []


def test_concat_list_1() -> None:
    """Tests that concat returns list_1 when list_2 is an empty list."""
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_concat_list_2() -> None:
    """Tests that concat returns list_2 when list_1 is an empty list."""
    assert concat([], [4, 5, 6]) == [4, 5, 6]


def test_concat() -> None:
    """Tests that concat functions properly when given two lists of random ints."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_sub() -> None:
    """Tests that sub returns a list of integers between the correct indecies from the initial list."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_negative_start() -> None:
    """Tests that sub returns a list that starts at the first int of the given list when index_1 is negative."""
    assert sub([10, 20, 30, 40], -1, 4) == [10, 20, 30, 40]


def test_sub_greater_end() -> None: 
    """Tests that sub returns a list whose final value is the last integer in the given list when index_2 is greater than the length of the initial list."""
    assert sub([10, 20, 30, 40], 1, 7) == [20, 30, 40]


def test_sub_length_zero() -> None:
    """Tests that sub returns an empty list when the initial list is empty."""
    assert sub([], 2, 4) == []


def test_sub_start_greater() -> None:
    """Tests that sub returns an empty list when index_1 is greater than the length of the given list."""
    assert sub([10, 20, 30, 40], 5, 7) == []


def test_sub_end_at_most_zero() -> None:
    """Tests that sub returns an empty list when index_2 is at most 0."""
    assert sub([10, 20, 30, 40], 1, 0) == []