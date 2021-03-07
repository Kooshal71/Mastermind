#ESA Project
import getpass#hide the input
print("You can use R,B,W,Y,P,O,G in place of Red, Blue, White, Yellow, Purple, Orange, Green")
i = getpass.getpass(prompt = "Please enter 4 colors, seperated by a space\n")
l = i.split(" ")#creation of the list
x = 0 # number of guesses
#print(l)
while 1:
    if x<12:
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
        print("You have ",(12-x),"guesses left")
    elif x == 12:
        print("You lost, all guesses are completed the correct answer is",l)
        break

