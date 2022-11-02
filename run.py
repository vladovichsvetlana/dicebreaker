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
#

# initialise arrays
# Icebreaker questions
questions = [
    "Q 1 chosen: What was one fun thing you did this summer?\n",
    "Q 2 chosen: What are your two favourite colours?\n",
    "Q 3 chosen: List three words that best describe you?\n",
    "Q 4 chosen: Name four of your favourite movies\n",
    "Q 5 chosen: List five of your favourite foods\n",
    "Q 6 chosen: Name six places you want to visit in your life\n",
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

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

# 2 player dice roll
def two_player_dice_roll():
    roll_dice = input("Player 1 - Press any key to roll dice:")
    result1 = random.randrange(1, 6)
    print("Player 1 you got a:")
    print(DICE_ART[result1])
    roll_dice = input("Player 2 - Press any key to roll dice:")
    result2 = random.randrange(1, 6)
    print("Player 2 you got a:")
    print(DICE_ART[result2])
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
    print(DICE_ART[q_chosen])
    return q_chosen


# Welcome message
print("Hello everyone! Welcome to the dicebreaker game!")

# Game loop with 6 attempts
play = 0
winner = 0
while play != "q":
    for x in range(1, 7):
        while winner == 0:
            winner = two_player_dice_roll()   # returns 0,1,2
        print("Player ", winner, "wins! - your get to answer the question")
        question_selected = one_player_dice_roll()  # return values 1 -6
        print("your selected question is:")
        print(questions[question_selected])
        input("Press any key when you have answered...")       
    play = input("Press any key to play again or q to quit")


