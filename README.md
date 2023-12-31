# mastermind

### RUN MASTERMIND LOCALLY ON YOUR DEVICE

1. Install Python - If you have not done so already, ensure that you have Python3 installed on your device/machine. You can install it from [Python's Official Website](https://www.python.org/).

2. Clone this repository - Open your terminal and run the following command to clone this Mastermind repository:

```
$ git clone https://github.com/gabeantonio/mastermind.git
```

3. Navigate to the project's directory - Move to the Mastermind project directory using the below command:

```
$ cd mastermind
```

4. Run the game - To play the game on your local terminal, execute the following command:

```
$ python3 init_mastermind.py
```

5. Follow the on-screen instructions - Once you execute the command stated above, please follow the on-screen instructions to play. Good luck, and happy guessing!

### TROUBLESHOOTING

1. If you happen to encounter any dependency issues, install the required Python packages:

Requests:

```
$ python3 -m pip install requests
```

Colorama:

```
$ pip install colorama
```

All other modules are built into Python3.

### HOW TO PLAY

1. Run the game using the command below:

```
$ python3 init_mastermind.py
```
2. Once you run the game, you'll have the option of increasing the game's difficulty before you start. If you want to play on hard difficulty, type "Yes" or "No" if you'd like to play the game on normal difficulty.

3. After picking your difficulty level, the game will begin, and you will be prompted to type your first guess. Please type in a combination of 4 numbers if you decided to play on normal difficulty and a combination of 5 numbers if you decided on hard difficulty. 

4. After each attempt at guessing the hidden combination, the computer will give you feedback. It will tell you how many correct numbers and positions you guessed, if any. The computer will also tell you if you got all the numbers incorrect. Additionally, the computer will keep track of your score and your previous guesses, and display them to you. 

    The scoring is as follows:

    - Guessing a correct number BUT not in the right position: +1 point
    - Guessing a correct number AND in the right position: +5 points

5. If you don't guess any correct numbers in a given attempt, the computer will ask you if you'd like a hint. Please type 'Yes' if you'd like one or 'No' if you don't.

6. You will have 10 attempts to figure out the hidden combination, so please use the feedback and hints from the computer to figure out the hidden combination. 

7. If you figure out the hidden combination before you run out of attempts, you win and the game will end. 

8. Similarly, if you fail to figure out the hidden combination and run out of attempts, you lose and the game will end.

9. Good luck!


### PROCESS

1. I plan on creating two scripts for this project: One script that will handle the interface on the command line, and one script that will handle the game logic.
2. mastermind.py will contain the game logic while init_mastermind will take care of the interface.
3. Starting with mastermind.py, I first want to initialize a hidden variable that will hold the random 4 number combination from the API. 
4. Then, I want to also create a list that will hold the player's guesses as the game progresses.
5. I want to create a variable that will hold the allowed attempts at guessing as well as the word length. (10 attemps, 4 numbers - as stated in the prompt)
6. I then want to write a function that will handle the winning logic.
7. Then, I can write logic for what to do when a user attempts a guess at the combination.
8. Now, I want to run the entriety of the game through a loop, so I will create a function that checks if the user still has remaining guesses.
9. Next, I want to create a function that will return the array that will hold all of the user's past guesses, so that the user can refer back to them.
10. Next, I want to make an API call to the Random Integer API so that we can use the returned value as the hidden combination. 
11. Now that I am able to get the random number combination, I want to write game logic that will check if the guess of the player is equal to the hidden combination, as well as check for any correct individual numbers and positions.
12. Then, based on the result of the guess, I want to display a message on the terminal.
13. I then want to add colors to the messages based on the contents.
14. Now that MVP is done, I want to implement a new feature: Giving the player a score that we can keep track of and display at the end of the game.
15. Based on my own decisions:

- User guesses a correct number BUT not in the right position: +1 point
- User guesses a correct number AND in the right position: +5 points

16. Next, I want to make it so that the game will give the player hints in case they need it.
17. I was able to add hints by adding logic to the part of the game where a user's entire guess has NO correct numbers.
18. I want to add timer functionality for the game.
19. I also want to add difficulty levels for the game.


### TECHNOLOGIES USED:
1. Python3
2. Python requests.2.31.0 (for API request handling)
3. Colorama (for game interface)
4. Python Random Module (for hint functionality)
5. Python Math module (for timer functionality)
6. Python Time Module (for timer functionality)