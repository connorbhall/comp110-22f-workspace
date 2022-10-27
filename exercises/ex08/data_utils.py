"""Dictionary related utility functions."""

__author__ = "730465288"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a CSV file."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Reads the columns of a CSV file."""
    result: list[str] = []
    for rows in table:
        item: str = rows[column]
        result.append(item)
    return result


def columnar(a_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Trasforms a table into a dictionary."""
    result: dict[str, list[str]] = {}
    row: dict[str, str] = a_table[0]
    for column in row:
        result[column] = column_values(a_table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Narows down a table to contain N amounts of rows."""
    result: dict[str, list[str]] = {}
    for column in table:
        head_list: list[str] = []
        i: int = 0
        if N > len(table):
            N = len(table)
        while i < N:
            head_list.append((table[column])[i])
            i += 1
        result[column] = head_list
    return result


def select(c_table: dict[str, list[str]], c_names: list[str]) -> dict[str, list[str]]:
    """Selects only the columns we care about."""
    result: dict[str, list[str]] = {}
    for columns in c_names:
        result[columns] = c_table[columns]
    return result


def concat(a_table: dict[str, list[str]], b_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables."""
    result: dict[str, list[str]] = {}
    for a_column in a_table:
        result[a_column] = a_table[a_column]
    for b_column in b_table:
        if b_column in result:
            for item in b_table[b_column]:
                (result[b_column]).append(item)
        else: 
            result[b_column] = b_table[b_column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequencies values in a lists."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result