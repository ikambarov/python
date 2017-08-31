_author_ = "ikambarov"

age = int(input("Please enter your age: "))

print("You age is {}".format(age))

if age >= 18:
    print("You are eligible to vote")

    if age >= 65:
        print("You are a senior")
    else:
        print("You are going to retire after {}".format(65-age))

else:
    print("You will be eligible to vote after {} years".format(18 - age))

    print("Finish")