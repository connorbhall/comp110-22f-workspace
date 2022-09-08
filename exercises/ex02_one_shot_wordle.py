"""EX02 - One Step Wordle - One Step Closer to Wordle."""

__author__ = "730465288"

SECRET: str = "python"
guess = str(len(SECRET))

user_word: str = str(input(f"What is your {guess} letter guess? "))

while len(user_word) != len(SECRET):
    user_word = str(input(f"That was not {guess} letters. Try again: "))

white_box: str = "\U00002B1C"
yellow_box: str = "\U0001F7E8"
green_box: str = "\U0001F7E9"

wordle: str = ""
i: int = 0
ii: int = 0
index: bool = False

while i < len(SECRET):
    if user_word[i] == SECRET[i]:
        wordle += str(green_box)
    else:
        while bool(index) is not True and ii < 6:
            if user_word[i] == SECRET[ii]:
                index = True
                wordle += str(yellow_box)
            else: 
                ii += 1
        if bool(index) == False:
            wordle += str(white_box)
        else: 
            index = False  
        ii = 0     
    i += 1
            
print(wordle)

if str(user_word) == str(SECRET):
    print(f"Woo! You got it!")
else:
    print("Not quite. Play again soon!")