"""Choose Your Own Adventure Game: Emojimon!"""


__author__ = "730465288"


def greet() -> None:
    """Greets player and assigns name to player global variable."""
    global player
    print("Welcome to the world of Emojimon!\nA world where both good and bad emojis are everywhere and it's your job to defeat them!")
    player = input("Let's get started! What should I call you? ")
    print(f"Excellent! Welcome to the world of Emojimon {player}!")
    tutorial_check: str = input("Before you get out there and fight, would you like me to show you the ropes? (Type 'yes' for tutorial): ")
    if tutorial_check == "yes":
        tutorial(tutorial_check)
    else:
        print(f"Perfect!\nCome on {player}! Let's go get those emojis!")



def tutorial(tutorial_value: int) -> None:
    """Gives new players a brief tutorial on how to play."""  
    



def main() -> None:
    """Runs emojimon!"""
    points: int = 0
    player: str = ""
    player_health: int = 100
    player_damage: 10
    
    emojis: dict[int, str]
    emojis[1] = ""
    emojis[2] = ""
    emojis[3] = ""
    emojis[4] = ""
    
    emojis_points: dict[str, int]
    emojis_points[] = 25
    emojis_points[] = 50
    emojis_points[] = 75
    emojis_points[] = 100

    emojis_damage: dict[str, int]
    emojis_damage[] = 10
    emojis_damage[] = 20
    emojis_damage[] = 35
    emojis_damage[] = 50

    emojis_health: dict[str, int]
    emojis_health[] = 75
    emojis_health[] = 100
    emojis_health[] = 150
    emojis_health[] = 300
    
    greet()
    while points < 500:
        if player_health == 0:
            return print(f"Oh no you died!\nYou scored {points} points!\nStart over and try again!")




if __name__ == "__main__":
    main()