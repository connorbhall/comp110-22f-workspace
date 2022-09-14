"""Structured Wordle - Another Step Closer to Wordle."""


__author__ = "730465288"


def contains_char(word: str, char: str) -> bool:
    """A boolean function to determine if a character is contained in a certain string."""
    assert len(char) == 1

    # i is a counting variable that allows each index of the word to be checked.
    i: int = 0

    # contains_char checks each index of the word to see if its str is equal to the str of char.
    # if any 1 index matches, the function returns True.
    # if the function cannot find a matching index between the word and the character, the function returns False. 
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """A function that returns one guess in Wordle in the form of colored boxes."""
    assert len(guess) == len(secret)
    from exercises.ex03_wordle import contains_char
   
    # imported contains_char function from above in order to check for matching indecies between 'guess' and 'secret'.
    # 'i' is a counting variable, 'wordle' is the returned string of boxes. 
    i: int = 0
    wordle: str = ""
    
    white_box: str = "\U00002B1C"
    yellow_box: str = "\U0001F7E8"
    green_box: str = "\U0001F7E9"
    
    # function enters while loop as long as 'i' is less than the length of 'secret'.
    # if any one index of 'guess' matches the same index in 'secret', a green box is concatenated to the str of wordle. 
    # else, the function runs contains_char between the secret word, and an index (determined by the counting variable).
    # if contains_char returns true, a yellow box is concatenated to 'wordle'.
    # if contains_char returns false, a white box is concatenated to 'wordle'.
    # 'i' is then increased by one, and the above code is ran on each index of 'guess'.
    # when the code exits the while loop, 'wordle' is returned.
    while i < len(secret):
        if guess[i] == secret[i]:
            wordle += str(green_box)
        elif contains_char(secret, guess[i]) is not False:
            wordle += str(yellow_box)
        else: 
            wordle += str(white_box)
        i += 1
    return wordle


def input_guess(expected_length: int) -> str:
    """Checks to make sure user's guess is the same as the input length."""
    # input_guess is a function that is used to assign 'user_word' to the user's input str.
    # function checks that the input has the same length as the user-inputed 'expected_length'.
    # if 'user_word' != 'expected_length', function prompts another chance to input a str that matches 'expected_length'.
    # if 'user_word' == 'expected_length', return 'user_word'. 
    user_word: str = input(f"Enter a {expected_length} character word: ")
    if len(user_word) == expected_length:
        return user_word
    else:
        while len(user_word) != expected_length:
            user_word = input(f"That wasn't {expected_length} chars! Try again: ")
        return user_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    from exercises.ex03_wordle import emojified
    from exercises.ex03_wordle import input_guess

    # main() combines all the defined functions above to create a structured wordle. 
    # emojified and input_guess are imported.
    # 'SECRET' is a str that is the correct input to win wordle.
    SECRET: str = "codes"
    i: int = 1
    check: bool = False

    # 'i' is a counting variable, 'check' is a variable used as a boolean expression.

    # function enters while loop if 'check' is not true and 'i' is less than or equal to number of turns (6).
    # each run of the loop, the turn number is printed.
    # 'guess' is assigned to the return of running input_guess with 'expected_length' being the length of 'SECRET'.
    # emojified function is ran with 'guess' as the 'guess' parameter and 'SECRET' as the 'word' parameter.
    # if str of 'guess' == str of 'SECRET', check is assigned to True, and a message declaring the user winning in an 'i' number of turns is printed. 
    # if check remains false, 'i' is increased by 1, and while loop continues. 
    # if i exceeds 6, function exits while loop and prints that user failed.
    while check is not True and i <= 6:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(len(SECRET))
        print(emojified(guess, str(SECRET)))
        if str(guess) == str(SECRET):
            check = True
            print(f"You won in {i}/6 of turns!")
        i += 1
    if check is not True and i > 6:
        print("X/6 - Sorry, try again tomorrow!")


# makes it possible to run program as a module, and makes main() able to be imported by other modules. 
if __name__ == "__main__":
    main()