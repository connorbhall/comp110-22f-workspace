"""Tests for the ex05 functions"""


__author__ = 730465288


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    list_1: list[int] = []
    assert only_evens([]) == []


def test_only_evens_all_odds() -> None:
    assert only_evens([1, 5, 3]) == []


def test_only_evens_all_fours() -> None:
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_only_evens() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_concat_empty() -> None:
    assert concat([], []) == []

def test_concat_list_1() -> None:
    assert concat([1, 2, 3], []) == [1, 2, 3]

def test_concat_list_2() -> None:
    assert concat([], [4, 5, 6]) == [4, 5, 6]

def test_concat() -> None:
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_sub() -> None:
    assert sub([10, 20 , 30 ,40], 1, 3) == [20, 30]

def test_sub_negative_start() -> None:
    assert sub([10, 20, 30, 40], -1, 4) == [10, 20, 30, 40]

def test_sub_greater_end() -> None: 
    assert sub([10, 20, 30, 40], 1, 7) == [20, 30, 40]

def test_sub_length_zero() -> None:
    assert sub([], 2, 4) == []

def test_sub_start_greater() -> None:
    assert sub([10, 20, 30, 40], 5, 7) == []

def test_sub_end_at_most_zero() -> None:
    assert sub([10, 20, 30, 40], 1, 0) == []