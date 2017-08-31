_author = "ikambarov"

randnumber = 7

count = 1

for i in range(0, 10):
    inputnumber = input("Please enter number between 0 - 9: ")

    if int(inputnumber) == randnumber:
        print("You got it!!!")
        break
    else:
        print("Please try again")
        count += 1

print("You were able to find random number in {} tries".format(count))
