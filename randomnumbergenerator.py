_author_ = "ikambarov"

import random

randomnumber = random.randrange(0, 10, 1)

print("Please enter number, try #1: ")
number = int(input())

for i in range(2, 11):
    if number == randomnumber:
        print("You got it!")
        found = 1
        break
    else:
        print("Please try again, try#{}: ".format(i))
        number = int(input())
        found = 0

if found == 0:
    print("You tried {} times and was not able to guess the number: {}".format(i-1, randomnumber))