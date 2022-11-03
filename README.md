This is a great first week of school activity. Help your students get to know each other with this casual game. Students are engaged in rolling dice, and matching their roll to a corresponding question that they answer loud to their group. All you need is some dice. The live site can be found here https://dashboard.heroku.com/apps/dicebreaker. Enjoy! 

Theme
As the Dicebreaker game is mainly text-based, I have added the ASCII diagram of dice faces to the game. When the user rolls the dice, the diagram artwork is printed with the chosen dice face.
User Experience

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
User Stories
As the user opens the game a “Welcome message” greets the players. 
"Hello everyone! Welcome to the dicebreaker game!"

Users are asked to type their names.  The error message appears if both players type the same name.
"I'm sorry but you need to use a slightly different name to player_one_name as I cannot tell you apart”
Both players are asked to roll the dice. Whoever get the highest number of the face dice wins the chance to start answering questions first:

Player … wins! - you get to answer the question

The winning player rolls the dice again. The question from the array auto populates according to the dice face number rolled by the player. The array has 6 questions (each question is assigned to certain dice face).

The dice face of the chosen question is displayed. The player will be asked to continue the game or to quit the game. If the player is choosing to quit the game the message will come up “Good Bye. Thank you for playing"


Python Logic 

I have prepared the following flowchart. This flowchart allowed me to follow the structure of the game during the process. 

Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Features

Future Features

Testing 

Technologies Used

The code was written in Python and the site was deployed using Heroku.

Python Libraries

Sys – to exit the programme. The sys module provides functions and variables used to manipulate different parts of the Python runtime environment, 

Random – used to generate or manipulate random numbers. It is used in a lot of games, lotteries or any application requiring a random number generation.  


Deployment

Credits

