"""Choose Your Own Adventure: Blackjack!"""


__author__ = "730465288"


points: int = 0
player: str = ""
bet_amount: int = 0
deck: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
dealer_hand: list[int] = []
player_hand: list[int] = []
dealer_total: int = 0
player_total: int = 0
player_bust: bool = False
dealer_bust: bool = False


def greet() -> None:
    """Greets the player."""
    global player
    player = input("Welcome to blackjack! What would you like to be called? ")
    print(".")
    print(f"Hello {player}! Let's get started!")
    print("-Each hand you'll bet a number of your points.\n-If you beat the dealer you win more points!")
    print("-However, if you lose, you'll lose points.\n-Don't hit zero points or it's game over!")
    print(f"Welcome to the table {player}! Go win some points!")
    print(".")
    print(f"Your starting point total is {points} points.")


def bet(bet_points: int) -> None:
    """Allows player to choose an amount of their points to bet on the hand."""
    global bet_amount
    print(".")
    bet_amount = int(input(f"{player}, How many points would you like to bet on this hand? "))
    while bet_amount == 0:
        bet_amount = int(input(f"Sorry {player}, but you can't bet 0! Try again: "))
    if bet_amount > bet_points:
        bet_amount = bet_points
        print(f"Oh, no! You only have {bet_points} points. Your bet is {bet_amount}.")

        
def dealer_hand_deal() -> list[int]:
    """Deals dealer's hand, ends turn if hidden number adds up to 21."""
    from random import randint
    global dealer_hand
    dealer_hand = [deck[randint(0, 13)], deck[randint(0, 13)]]
    global dealer_total
    dealer_total = 0
    for card in dealer_hand:
        dealer_total += card
    return dealer_hand
    

def player_hand_deal() -> list[int]:
    """Deals player's hand."""
    from random import randint
    global player_hand
    player_hand = [deck[randint(0, 13)], deck[randint(0, 13)]]
    global player_total
    player_total = 0
    for card in player_hand:
        player_total += card
    return player_hand


def hit() -> bool: 
    """Allows player to add another number to their hand/total."""
    from random import randint
    hit_again: str = "hit"
    while hit_again == "hit":
        new_card: int = deck[randint(0, 13)]
        global player_hand
        player_hand.append(new_card)
        print(player_hand)
        global player_total
        player_total += new_card
        if player_total == 21:
            print(f"Your new total is: {player_total}")
            return False
        elif player_total > 21:
            return True
        print(f"Your new total is: {player_total}")
        hit_again = input("Would you like to hit again? ('hit' or 'stand') ")  
        print(".")
    return False      
        

def double() -> bool:
    """Allows player to double their initial bet and hit once."""
    from random import randint
    global bet_amount
    global points
    bet_amount = 2 * bet_amount
    if bet_amount > points:
        bet_amount = points
        print(f"You only have {points} points! You now have {bet_amount} points on this hand!")
    else:
        print(f"You now have {bet_amount} points on this hand!")
    print(".")
    double_card = deck[randint(0, 13)]
    global player_hand
    player_hand.append(double_card)
    print(player_hand)
    global player_total 
    player_total += double_card
    if player_total > 21:
        return True
    return False


def player_turn() -> None:
    """Forces player to make a decision whether to hit, stand, or double."""
    print(".")
    print(f"Okay {player}, you can either:\n-Stand (keep ur current total.)\n-Hit (add another number to your total.)\n-Double (double your bet size and hit once.)")
    print(".")
    player_decision: str = input("Would you like to hit, stand, or double? (Type corresponding answer) ")
    print(".")
    if player_decision == "hit":
        global player_bust
        player_bust = hit()
        if player_bust is False:
            return print(f"{player}'s final total: {player_total}\nDealer's turn...")
        else:
            return print(f"Oh no! You busted at {player_total}")
    elif player_decision == "stand":
        return print(f"{player}'s final total: {player_total}\nDealer's turn...")
    elif player_decision == "double":
        player_bust = double()
        if player_bust is False:
            return print(f"{player}'s final total: {player_total}\nDealer's turn...")
        else:
            return print(f"Oh no! You busted at {player_total}")
    

def dealer_turn() -> None: 
    """After player's turn, dealer can either hit or stand."""
    from random import randint
    global dealer_hand
    global dealer_total
    print(".")
    print(dealer_hand)
    print(f"Dealer's total is: {dealer_total}")
    print(".")
    while dealer_total <= 16:
        new_card: int = deck[randint(0, 13)]
        dealer_hand.append(new_card)
        dealer_total += new_card
        print(".")
        print("The dealer has to hit!")
        print(dealer_hand)
        if dealer_total > 21:
            print(f"The dealer busted at {dealer_total} points!")
            print(".")
            global dealer_bust
            dealer_bust = True
        else:
            print(f"The dealer's new total is: {dealer_total}")
            print(".")


def payout(win_loss: int, total_points: int) -> int:
    """Determines if player wins or loses and then gives or takes points."""
    print(".")
    global bet_amount
    if win_loss == 0:
        total_points -= bet_amount
        print(f"Tough loss, Your new point total is: {total_points}")
        return total_points
    elif win_loss == 1:
        total_points += bet_amount
        print(f"Nice win! Your new point total is: {total_points}")
        return total_points
    elif win_loss == 2:
        print(f"You and the dealer pushed! You stay at {total_points} points!")
        return total_points
    else:
        return total_points
    

def play() -> bool:
    """Asks player if they want to play another hand, or allows them to quit."""
    print(".")
    if points <= 0:
        print(".")
        print(f"Oh no {player}! You are out of points! Better luck next time!")
        return False
    else:
        play_or_not: str = input(f"{player}, would you like to play another hand? ('yes' to continue, 'no' to quit) ")
        if play_or_not == "no":
            print(".")
            print(f"Sad to see you go {player}! Come soon and play some more!")
            return False
        else:
            return True
    

def main() -> None:
    """Runs Blackjack."""
    play_again: bool = True
    mystery_card: str = "\U0001F0CF"
    global points
    points = 100
    greet()
    while points > 0 and play_again is True:
        bet(points)
        dealer_hand_view: list[str] = [str(dealer_hand_deal()[0]), str(mystery_card)]
        print(".")
        print(f"Dealer's hand: {dealer_hand_view}")
        print(f"Your hand: {player_hand_deal()}, Total: {player_total}")
        if player_total == 21 and dealer_total == 21:
            print("You both got Blackjack!!!")
            points = payout(2, points)
        elif dealer_total == 21:
            print("Dealer has Blackjack!")
            points = payout(0, points)
        elif player_total == 21:
            print("You have Blackjack!")
            points = payout(1, points)
        else:
            global player_bust
            player_bust = False
            player_turn()
            if player_bust is True:
                points = payout(0, points)
            else:
                global dealer_bust
                dealer_bust = False
                dealer_turn()
                if dealer_bust is True:
                    points = payout(1, points)
                elif dealer_total > player_total:
                    points = payout(0, points)
                elif dealer_total < player_total:
                    points = payout(1, points)
                elif dealer_total == player_total:
                    points = payout(2, points)
        play_again = play()
    exit()
        
        
if __name__ == "__main__":
    main()