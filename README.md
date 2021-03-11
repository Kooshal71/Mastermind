# Mastermind
Computer Project
Objectives: The program is made to recreate the board game mastermind
 Description:
•	Mastermind is a board game which requires 2 players
•	One of the players will set a certain sequence of colors and the other player will have to guess the colors in the same order
•	The player guessing will only have a certain number of guesses after which the player who set the colors will win the game
•	To aid the player who is guessing the number of correct colors and the number of correct positions will be revealed without revealing the name of the colors
•	The player who has set the colors cannot change them during the game, this can only happen at the beginning of a new game
•	The colors will be selected only from a specified provided set of colors
Outcome:
 A working simulation of the game without the implementation of GUI
Structure of I/O: 
Both the input and output will be taken and given respectively in the terminal of the code itself. 
Computer Version:
		In this version only the player will only be able to guess and not set any colors as he is playing against the computer. He will be requested to enter 1 color at a time for a specific position
Player Version:
	In this version the player will be able to set the colors in a specified position and the player will be able to guess the colors when the terminal requests him to enter 1 color for a position at a time

Python Modules:
1.	Random – This was used to randomly select a color from the given set of colors
2.	Getpass – This was used to hide the entry of the first player during the player version

