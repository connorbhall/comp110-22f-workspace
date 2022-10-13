"""EX07 - Using functions to alter dictionaries."""


__author__ = 730465288


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    dict_2: dict[str, str] = {}
    for key in dict_1:
        value: str = dict_1[key]
        dict_2[value] = key
    if len(dict_2) < len(dict_1):
        raise KeyError("Keys can't be repeated.")
    return dict_2


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the most frequent color in a list."""
    counting_color: dict[str, int] = {}
    color_list: list[str] = []
    for person in color_dict:
        color_list.append(color_dict[person])
    for color in color_list:
        counting_color[color] = 0
    for color in color_list:
        if str(color) in counting_color:
            counting_color[color] += 1
    common_color: str = color_list[0]
    x: int = 0
    for key in counting_color:
        if counting_color[key] > 1:
            if x == 0:
                x = counting_color[key]
                common_color = key
            elif counting_color[key] > x:
                x = counting_color[key]
                common_color = key
    print(counting_color)
    return common_color


def count(list_1: list[str]) -> dict[str, int]:
    """Counts the frequency of items in a list and returns a dictionary of the values."""
    counting: dict[str, int] = {}
    for item in list_1:
        counting[item] = 0
    for item in list_1:
        if str(item) in counting:
            counting[item] += 1
    return counting