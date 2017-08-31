_author_ = "ikambarov"

pyramidsize = 10
star = 0

for i in range(0, pyramidsize):
    # This loop is printing spaces
    for j in range(0, (pyramidsize - i)):
        print(" ", end='')
    # This loops is printing stars
    for k in range(0, 2 * (i + 1) - 1):
        if i != pyramidsize - 1:
            if k == 0:
                print("*", end='')
            elif k == (2 * i):
                print("*", end='')
            else:
                print(" ", end='')
        else:
            if star == 0:
                print("*", end='')
                star = 1
            else:
                print(" ", end='')
                star = 0
    # This print is printing new lines
    print("")
