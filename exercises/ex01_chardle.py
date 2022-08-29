"""EX01 - Chardle - A Cute step toward Wordle"""

__author__ = "730465288"

user_word: str = str(input("Enter a 5-character word: "))
if len(str(user_word)) != 5:
    print("Error: Word must contain 5 charcters")
    exit()

user_character: str = str(input("Enter a single character: "))
if len(str(user_character)) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + str(user_character) + " in " + str(user_word))

if user_character == user_word[0]:
    print (user_character + " found at index 0")
if user_character == user_word[1]:
    print (user_character + " found at index 1")
if user_character == user_word[2]:
    print (user_character + " found at index 2")
if user_character == user_word[3]:
    print (user_character + " found at index 3")
if user_character == user_word[4]:
    print (user_character + " found at index 4")

indecies: int = 0
if user_character == user_word[0]:
    indecies = indecies + 1
if user_character == user_word[1]:
    indecies = indecies + 1
if user_character == user_word[2]:
    indecies = indecies + 1
if user_character == user_word[3]:
    indecies = indecies + 1
if user_character == user_word[4]:
    indecies = indecies + 1

if indecies == 0:
    print("No instances of " + user_character + " found in " + user_word)
if indecies == 1:
    print("1 instance of " + user_character + " found in " + user_word)
if indecies > 1:
    print(str(indecies) + " instances of " + user_character + " found in " + user_word)