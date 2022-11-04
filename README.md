![DICEBREAKERINTRO](https://user-images.githubusercontent.com/107796276/200064016-aaedbe5d-e0f7-4def-83cb-e5d1f0b3ef04.jpg)

Dicebreaker

This is a great first week of school activity. Help your students get to know each other with this casual game. Students are engaged in rolling dice, and matching their roll to a corresponding question that they answer loud to their group. All you need is some dice. The live site can be found here https://dashboard.heroku.com/apps/dicebreaker. Enjoy! 

Theme

As the Dicebreaker game is mainly text-based, I have added the ASCII diagram of dice faces to the game. When the user rolls the dice, the diagram artwork is printed with the chosen dice face.

![diceASCII](https://user-images.githubusercontent.com/107796276/199841533-2e3b7813-cc20-4581-8236-d0d3d760ba66.jpg)

User Stories

As the user opens the game a “Welcome message” greets the players. 
"Hello everyone! Welcome to the dicebreaker game!"

![hellomessage (2)](https://user-images.githubusercontent.com/107796276/200068302-a91d79bd-8955-4ebf-8552-6d1654cbaa08.jpg)

Users are asked to type their names:  

![hellomessage](https://user-images.githubusercontent.com/107796276/200068953-b505af08-102e-4fcb-80b8-09e7d0ef7fed.jpg)

Both players are asked to roll the dice: 

![svetlanagot2](https://user-images.githubusercontent.com/107796276/200068380-8a6812e7-7811-4082-bacd-70e889705a42.jpg)

In case of the draw, the players are asked to roll the dice again:

![drawmessage](https://user-images.githubusercontent.com/107796276/200068275-c0ab9651-79b8-47bb-a30e-9ac8ddd8116b.jpg)

Whoever get the highest number of the face dice wins the chance to start answering questions first:

Player … wins! - you get to answer the question

![mariawins](https://user-images.githubusercontent.com/107796276/200068368-e78af02e-07b2-49b2-a796-36236a178d3f.jpg)

The winning player rolls the dice again. The question from the array auto populates according to the dice face number rolled by the player. 

![mariaanswersquestions](https://user-images.githubusercontent.com/107796276/200068344-f0dd5105-3810-41ee-a26b-f24f8677c6a3.jpg)

The array has 6 questions (each question is assigned to certain dice face).

The dice face of the chosen question is displayed. The player will be asked to continue the game or to quit the game. If the player is choosing to quit the game the message will come up “Good Bye. Thank you for playing".

![playorquitmessage](https://user-images.githubusercontent.com/107796276/200068329-fa859d91-3fa6-4325-92f6-343bc589773c.jpg)

Invalid name entry

If both user enter the same name they will be asked to enter the name again. The following message will come up:
"I'm sorry but you need to use a slightly different name to player_one_name as I cannot tell you apart”

Python Logic 

I have prepared the following flowchart. This flowchart allowed me to follow the structure of the game during the process. 

Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Future Features

More players could be added to the game in the future as the current code is written for 2 players only

Testing 

One of the obstacles during the game development was getting the ASCII design dice face. The images were not coming up getting broken on the lines. 

Technologies Used

The code was written in Python and the site was deployed using Heroku which is available via the link https://dashboard.heroku.com/apps/dicebreaker/deploy/github.

Python Libraries

Sys – to exit the programme. The sys module provides functions and variables used to manipulate different parts of the Python runtime environment, 

Random – used to generate or manipulate random numbers. It is used in a lot of games, lotteries or any application requiring a random number generation.  

Black v22.10.0 - the uncompromising Python code formatter. Black reformats entire files in place.

Unfixed bugs

No bugs found at the time of deploying the game on Heroku. 

Validators Testing

The code has been tested by running it through the PeP8. Almost all of the errors that have been encountered were due to trailing whitespaces or either too many or not enough blank lines.

There were some issues with the code being too long in some cases; however, after validating it in Black Python code formatter all issues were resolved. No errors were found at the final stage.

![Screenshot_20221102_200354 (1)](https://user-images.githubusercontent.com/107796276/199847392-844c2e7a-f338-4cbd-985e-3de32d93d005.png)

Browser Testing

The programme has been tested on Google Chrome, Firefox and Safari without any issues.

Deployment

The website was deployed by following the steps below:

Log in Heroku.

Select 'New' and and then click 'Create new app'.

Decide on the name for the app, region and press on 'Create app' button.

Go to 'Settings' section.

Buildpacks will get generated. All future dependencies will be generated too (python and node.js). They install future dependencies that are needed outside of the requirements file. 

Github is then connected after clicking on "Deploy" button. 

The name of the correct repositery would need to be chosen first. It should then need to be connected via "Connect" button. The choice of the automatic and manual deployment will be offered too. 

Once the button "Click deploy branch" is pressed the task is completed. 

Credits

I used the following resources:

* tutorial for generation and display of ASCII diagram - https://realpython.com/python-dice-roll/

* for guidance on how to display a multiline string - https://stackoverflow.com/questions/10660435/how-do-i-split-the-definition-of-a-long-string-over-multiple-lines

* how to stop the programme - https://www.hashbangcode.com/article/stopping-code-execution-python

* tutorial on python - https://pythonbasics.org/multiple-return/

* Playground for Black - the uncompromising Python code formatter - https://black.vercel.app/





