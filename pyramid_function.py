_author_ = "ikambarov"

def printline(val1, val2):
    for i in range(0, val1):
        print(" ", end='')

    for j in range(0, val2):
        print("*", end='')


pyramidsize = 20
for k in range(1, pyramidsize):
    printline((pyramidsize - k), (k * 2 - 1))
    print("")

