import random
roll_dice = input("Write start to dice roll: ")

if roll_dice == "start":
   possible_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(possible_results)
   print("Result of dice rolling is : " + str(result))
