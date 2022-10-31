# Import required modules
import random
import sys

# Welcome message
print("Hello everyone! Welcome to the dicebreaker game!")

# Start the game
a = input("To start the game type yes and to quit type no")
if a.lower() == "no":
    sys.exit()
else:
    print('''Let's start the dicebreaker game.
        1. Players throw the dice one after another answering the questions.\n'
        2. There are 6 questions on the list and 6 attempts to throw dice.\n'
        3. If dice has number 1, question 1 is to be answered and so on.\n'
        4. Game can be restarted after 6 attempts or stopped''')

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
