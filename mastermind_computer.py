#ESA Project
import random
print("You can use R,B,W,Y,P,O,G in place of Red, Blue, White, Yellow, Purple, Orange, Green")
c1 = random.choice(['R','B','W','Y','P','O','G'])
c2 = random.choice(['R','B','W','Y','P','O','G'])
c3 = random.choice(['R','B','W','Y','P','O','G'])
c4 = random.choice(['R','B','W','Y','P','O','G'])
l = [c1,c2,c3,c4]
x = 0
t = int(input("Enter the number of guesses you would like to play with"))
while t<0:
    print("Please enter a value greater than 0")
    t = int(input("Enter the number of guesses you would like to play with"))
while 1:
    if x<t:
        m = 0 #counter for correct color
        n = 0 #counter for correct position
        c1 = input("Enter first color\n")
        if c1.upper() in l:
            #print("Correct color")
            m += 1
            if c1.upper() == l[0]:
                #print("Correct position")
                n += 1
        c2 = input("Enter second color\n")
        if c2.upper() in l:
            #print("Correct color")
            m += 1
            if c2.upper() == l[1]:
                #print("Correct position")
                n += 1
        c3 = input("Enter third color\n")
        if c3.upper() in l:
            ##print("Correct color")
            m += 1
            if c3.upper() == l[2]:
                #print("Correct position")
                n += 1
        c4 = input("Enter fourth color\n")
        if c4.upper() in l:
            #print("Correct color\n")
            m += 1
            if c4.upper() == l[3]:
                #print("Correct position")
                n += 1
        x += 1
        print("There are " ,m, " Correct colors and " ,n, " of them are in the correct position.")
        if [c1.upper(),c2.upper(),c3.upper(),c4.upper()] == l:
            print("You won and you did it in " ,x, " guesses")
            break
        print("would you like to continue playing?")
        a = input("Press Y to continue and N to stop")
        if a == 'Y' or a == 'y':
            print("You have chosen to continue playing")
            pass
        elif a == 'n' or a == 'N':
            print("You have chosen to stop playing")
            break
        print("You have ",(t-x),"guesses left")
    elif x == t:
        print("You lost, all guesses are completed the correct answer is",l)
        break

