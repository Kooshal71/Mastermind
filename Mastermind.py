print("Would you like to play MasterMind?")
m = input("Enter 'Y' to Play and 'N' to Quit\n")
j = 0 #counter for games played
while m == 'Y' or m == 'y':
    print("Would you like to play against a Computer or a another Player?")
    x = input("Enter 'C' to play against Computer and 'P' to play against another Player\n")
    if x == 'P' or x == 'p':
        import Mastermind_player
    elif x == 'C' or x == 'c':
        import mastermind_computer
    else:
        print("Please enter a valid choice.")
    print("Would you like to play MasterMind again?")
    #print("Would you like to play again.")
    m = input("Enter 'Y' to Play and 'N' to Quit\n")
    j += 1
if m == 'n' or m == 'N':
    print("You have played",j,"games")
    #print("You have played",j,"games and won",i,"out of them.")
else:
    print("Please enter a valid choice.")
''' errors
if the color repeats then still correct color is shown this logic must be changed
there should be a counter which counts the number of games won and number of games played
'''
