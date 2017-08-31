_author_ = "ikambarov"

numbers = [1, 34, 67, 0, 4, 999, -21, 17]
sortednumber = list()

for i in range(0, len(numbers)):
    smallnum = numbers[0]

    for num in numbers:
        if smallnum > num:
            smallnum = num

    sortednumber.append(smallnum)
    del numbers[numbers.index(smallnum)]

print(sortednumber)