'''
colors = []
num = int(input("Please enter the number of colors"))
i = 1
original = []
while num:
    colors.append(input("Please enter ",i,"color."))
    num = num - 1
    if colors[i-1] in original:
        #counter increases
        pass
        if colors[i-1] == original[i-1]:
            #counter increases
            pass
'''
import random
original = []
original.append(random.choice(['R','B','W','Y','P','O','G']))
print(original)