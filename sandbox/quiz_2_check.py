def v(input: str) -> str:
    result: str = ""
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    i: int = 0
    x: int = 0
    is_vowel: bool = False
    while i < len(input):
        is_vowel = False
        x = 0
        while x < len(vowels):
            if input[i] == vowels[x]:
                is_vowel = True
            x += 1
        if is_vowel is True:
            if i % 3 != 0:
                result += input[i]
        if is_vowel is False:
            if i % 3 == 0:
                result += input[i]
        i += 1
    return result

def a(input: dict[str, list[int]]) -> dict[str, float]:
    result: dict[str, float] = {}
    average: list[int] = []
    for name in input:
        average = []
        average = input[name]
        i: int = 0
        grade: float = 0.0
        grade = 0.0
        while i < len(average):
            grade += average[i]
            i += 1
        grade = grade / len(average)
        result[name] = grade
    return result

def o(input: list[int]) -> list[int]:
    result: list[int] = []
    i: int = 0
    while i < len(input):
        if i % 2 == 0:
            result.append(input[i])
        i += 1
    result_2: list[int] = []
    i = 0
    while i < len(result):
        if result[i] % 2 != 0:
            result_2.append(result[i])
        i += 1
    return result_2

def zoo(input: dict[str, list[int]]) -> list[str]:
    result: list[str] = []
    x: int = 0
    i: int = 0
    animal: str = ""
    while i < 3:
        for exhibit in input:
            if (input[exhibit])[i] > x:
                x = (input[exhibit])[i]
                animal = exhibit
        result.append(animal)
        i += 1
    return result