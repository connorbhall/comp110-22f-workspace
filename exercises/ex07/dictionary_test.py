"""EX07 - Test functions in order to test dictionary.py functions."""


__author__ = 730465288


from dictionary import invert, favorite_color, count


def test_invert_with_all_different() -> None:
    """Inverts a dictionary of all different strings."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_single_long_strings() -> None:
    """Inverts a dictionary of single words."""
    assert invert({'cat': 'apple'}) == {'apple': 'cat'}


def test_invert_raise_key_error() -> None:
    """Checks to see if repeating keys result in a KeyError."""
    import pytest
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_empty_dict() -> None:
    """Ensures that invert function returns an empty dict when given an empty dict."""
    assert invert({}) == {}


def test_favorite_color_norm() -> None:
    """Returns favorite color of one multiple color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_multiple() -> None:
    """Ensures first appearing color is returned when multiple colors repeated."""
    assert favorite_color({"Marc": "yellow", "Connor": "red", "Victor": "red", "Casey": "yellow"}) == "yellow"


def test_favorite_color_all() -> None:
    """Ensures correct favorite is returned even when a different multiple comes first."""
    assert favorite_color({"Marc": "yellow", "Connor": "red", "Victor": "red", "Casey": "yellow", "Nick": "yellow"}) == "yellow"


def test_favorite_color_one() -> None:
    """Tests if none repeat, first color is returned."""
    assert favorite_color({"Marc": "yellow", "Connor": "red", "Victor": "blue"}) == "yellow"


def test_count_once_each() -> None:
    """Tests that count will return a dictionary value of 1 for each key."""
    assert count(['a', 'b', 'c', 'd']) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}


def test_count_one_key() -> None:
    """Tests that multiple single keys will return one key and one int."""
    assert count(['a', 'a', 'a', 'a', 'a']) == {'a': 5}


def test_count_rand_list() -> None:
    """Tests the functionality of count function."""
    assert count(['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'e']) == {'a': 2, 'b': 3, 'c': 1, 'd': 2, 'e': 1}



def test_count_empty_list() -> None:
    """Ensures that count will return an empty dictionary if list is empty."""
    assert count([]) == {}