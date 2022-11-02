# Import required modules
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


# 2 player dice roll
def two_player_dice_roll():
    result1 = 0
    result2 = 0
    roll_dice = input("Player 1 - Press any key to roll dice:")
    result1 = random.randrange(1, 6)
    print("Player 1 you got a:")
    generate_dice_faces_diagram(result1)
    roll_dice = input("Player 2 - Press any key to roll dice:")
    result2 = random.randrange(1, 6)
    print("Player 2 you got a:")
    generate_dice_faces_diagram(result2)
    if result1 > result2:
        chosen = 1
    elif result1 < result2:
        chosen = 2
    else:
        chosen = 0
    return chosen


# 1 player dice roll
def one_player_dice_roll():
    roll_dice = input("Press any key to roll dice to get random question:")
    q_chosen = random.randrange(1, 6)
    print("Player you got a:")
    generate_dice_faces_diagram(q_chosen)
    return q_chosen


# Welcome message
print("Hello everyone! Welcome to the dicebreaker game!")

# Game loop with 6 attempts
play = 0
next_question = 0
while play != "q":
    while next_question != "q":
        winner = 0
        # loop id a draw
        while winner == 0:
            winner = two_player_dice_roll()   # returns 0,1,2
        # choose winner
        print("Player ", winner, "wins! - you get to answer the question")

        # roll die to select question
        question_selected = one_player_dice_roll()  # return values 1 -6
        input("Press any key to see your question...")
        print("your selected question is:")
        # get a question (-1 to start count at 0 for array)
        print(questions[question_selected-1])
        input("Press any key when you have answered...")
        next_question = input("Press any key to play again or q to quit")
    # end while loop

    play = input("Press any key to restart or q to quit")
# end while loop

print("Good Bye. Thank you for playing")

sys.exit()
