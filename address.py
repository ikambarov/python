_author_ = "ikambarov"

for i in range(0, 1000):
    position = input("Where do you live, n/s/w/e?: ")

    address = int(input("Please enter your address(Number): "))

    if position == "n" or position == "N":
        if (address > 0) and (address <= 1600):
            print("You live at downtown")
        elif address <= 7200:
            print("You live at North side")
        else:
            print("You live at North suburbs")
    elif position == "s":
        if (address > 0) and (address <= 1200):
            print("You live at downtown")
        elif address <= 9500:
            print("You live at South side")
        else:
            print("You live at South suburbs")
    elif position == "e":
        if (address > 0) and (address <= 400):
            print("You live at downtown")
        else:
            print("You live at Lake")
    elif position == "w":
        if (address > 0) and (address <= 800):
            print("You live at downtown")
        elif address <= 8400:
            print("You live at West side")
        else:
            print("You live at West suburbs")



