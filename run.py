import random 

questions = ["Q 1 chosen: What was one fun thing you did this summer?", "Q 2 chosen: What are your two favourite colours?", "Q 3 chosen: List three words that best describe you?", "Q 4 chosen: Name four of your favourite movies", "Q 5 chosen: List five of your favourite foods", "Q 6 chosen: Name six places you want to visit in your life"]
play = 0
while play != "q":
    for x in range(1, 7):
        roll_dice = input("Press any key to roll dice:")
    result = random.randrange(1, 6)
    print(questions[result])
    x += 1

    play = input("Press any key to play again or q to quit")

print("Good Bye. Thank you for playing")
