# pylint: disable=missing-module-docstring\n
# pylint: disable=missing-class-docstring\n
# pylint: disable=missing-function-docstring\n

# Import required modules
import random
import sys

# Welcome message
print("Hello everyone! Welcome to the dicebreaker game!")

# Start the game
a = input("To start the game type yes and to quit type no:")
if a.lower() == "no":
    sys.exit()
else:
    print('''Let's start the dicebreaker game.
        1. Players throw the dice one after another answering the questions.\n'
        2. There are 6 questions on the list and 6 attempts to throw dice.\n'
        3. If dice has number 1, question 1 is to be answered and so on.\n'
        4. Game can be restarted after 6 attempts or stopped''')

# starting the scores with zero
player1_score = 0
player2_score = 0

# Generating random values for both players
player1_value = random.randint(1, 6)
player2_value = random.randint(1, 6)

# Stating the players
print("Player 1 rolled: ", player1_value)
print("Player 2 rolled: ", player2_value)

# Comparison of values
if player1_value > player2_value:
    print("player 1 wins.")
    player1_score = player1_score + 1  
elif player2_value > player1_value:
    print("player 2 wins")
    player2_score = player2_score + 1
else:
    print("It's a draw")

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


def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

# Return diagram of dice faces from dice_values


def generate_dice_faces_diagram(dice_values):
    dice_faces = _get_dice_faces(dice_values)
    

def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces
print(f"\n{dice_face_diagram}") # Display the diagram

# To introduce the dicebreaker questions
questions = [
    "Q 1 chosen: What was one fun thing you did this summer?",
    "Q 2 chosen: What are your two favourite colours?", 
    "Q 3 chosen: List three words that best describe you?",
    "Q 4 chosen: Name four of your favourite movies", 
    "Q 5 chosen: List five of your favourite foods", 
    "Q 6 chosen: Name six places you want to visit in your life",
]

# Game loop with 6 attempts
play = 0
while play != "q":
    for x in range(1, 7):
        roll_dice = input("Press any key to roll dice:")
        result = random.randrange(1, 6)
        print(questions[result])
        x += 1

    play = input("Press any key to play again or q to quit")

# Exiting game\n
print("Good Bye. Thank you for playing")
