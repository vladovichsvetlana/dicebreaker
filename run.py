import random
roll_dice = input("Write start to dice roll: ")

if roll_dice == "start":
   possible_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(possible_results)
   print("Result of dice rolling is : " + str(result))

if result == '1':
   print("What was one fun thing you did this summer?")

elif result == "2":
   print("What are your two favourite colours?")

elif result == "3":
   print ("List three words that best describe you?")

elif result == "4":
   print ("Name four of your favourite movies")

elif result == "5":
   print ("List five of your favourite foods")

elif result == "6":
   print ("Name six places you want to visit in your life")

else:
print('Thanks For Playing')
break
