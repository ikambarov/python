_author_ = "ikmabarov"

#List
fruits = ["mellon", "srawberry", "apple"]
print(fruits)

#Tuple
cars = ("bmw", "audi", "mercedes")
print(cars)

#Sets
pets = {"cat", "fish", "parrot", "horse"}
print(pets)

#Dictionary
camry = {"color": "silver", "engine": "2.4", "doors": 4, "mpg" : 25 }
print(camry)

for val in camry.keys():
    print("My Camry's " + val + " is " + str(camry[val]))
