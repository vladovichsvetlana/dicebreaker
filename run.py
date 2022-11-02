import random
import sys
# Game for Selecting Icebreaker questions
# initialise arrays
# loop for 6 times
# Choose player - call 2 player dice roll
# Calc winner
# Winner to answer
# Choose question - call to 1 player dice roll
# Select question
# Has question been answered y/n?
# end loop
# initialise arrays
# Icebreaker questions
questions = [
    "Q 1 chosen: What was one fun thing you did this summer?",
    "Q 2 chosen: What are your two favourite colours?",
    "Q 3 chosen: List three words that best describe you?",
    "Q 4 chosen: Name four of your favourite movies",
    "Q 5 chosen: List five of your favourite foods",
    "Q 6 chosen: Name six places you want to visit in your life",
]
# Dice images
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = 5
def generate_dice_faces_diagram(dice_value):
    """Return an ASCII diagram of dice face from `dice_value`.
    The string returned contains an ASCII representation of a die.
    For example, if `dice_values = 4` then the string returned looks like this:
    ~~~~~~~~~~~~~~~~~~~ RESULT ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐
    │  ●   ●  │
    │         │
    │  ●   ●  │
    └─────────┘
    """
    # Generate a list containing the dice rows
    for x in range(5):
        print(DICE_ART[dice_value][x])
    return
def two_player_dice_roll(player_one_name, player_two_name):
    """This method manages the logic of dice rolling for
    two players and returns which player scored the highest
    """
    result1 = 0
    result2 = 0
    input(f"{player_one_name} - Press any key to roll dice:")
    result1 = random.randrange(1, 6)
    print(f"{player_one_name} you got a:")
    generate_dice_faces_diagram(result1)
    input(f"{player_two_name} - Press any key to roll dice:")
    result2 = random.randrange(1, 6)
    print(f"{player_two_name} you got a:")
    generate_dice_faces_diagram(result2)
    if result1 > result2:
        chosen = 1
    elif result1 < result2:
        chosen = 2
    else:
        print(
            f"Oh wow, you both rolled a {result1}, you will have to roll again!"
        )
        chosen = 0
    return chosen
def one_player_dice_roll(name):
    """This method rolls the dice for one player
    and returns the result
    """
    input(f"OK {name}, press any key to roll dice to get a random question:")
    q_chosen = random.randrange(1, 6)
    print(f"and {name} rolls a:")
    generate_dice_faces_diagram(q_chosen)
    return q_chosen
def get_name(number):
    """This gets the players name with validation
    and returns it.
    """
    player_name = ""
    while player_name == "":
        player_name = (
            input(f"Please enter your name player {number}\n").strip().lower()
        )
        if player_name == "":
            print("Hey, enter a name and don't try to just enter spaces.")
            continue
        return player_name
def start_game():
    """This method starts and handles the game flow and is
    called by the main method
    """
    print("Hello everyone! Welcome to the dicebreaker game!")
    # Get the users names
    player_one_name = get_name("one")
    player_two_name = get_name("two")
    while player_one_name == player_two_name:
        print("I'm sorry but you need to use a slightly different name to ")
        print(f"{player_one_name} as I cannot tell you apart")
        player_two_name = get_name("two")
    # Game loop with 6 attempts
    play = 0
    next_question = 0
    while play != "q":
        while next_question != "q":
            winner = 0
            # loop id a draw
            while winner == 0:
                winner = two_player_dice_roll(player_one_name, player_two_name)
            # choose winner
            if winner == 1:
                winner = player_one_name
                loser = player_two_name
            else:
                winner = player_two_name
                loser = player_one_name
            print(f"Player {winner}, wins! - you get to answer the question")
            # roll die to select question
            question_selected = one_player_dice_roll(
                winner
            )  # return values 1 -6
            input("Press any key to see your question...")
            print("your selected question is:")
            # get a question (-1 to start count at 0 for array)
            print(questions[question_selected - 1])
            print(f"Now {winner} you have to face {loser} and tell them and\n")
            input("Press any key when you have answered...")
            next_question = input(
                f"Now {winner} please press any key to play again or q to quit"
            )
            if next_question == "q":
                # end while loop
                print("Good Bye. Thank you for playing")
                sys.exit()
if __name__ == "__main__":
    start_game()













