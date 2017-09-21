# Class is a a template to create objects
# Object: an instance of a class
# Instantiate: create an instance of a class
# Method: function defined in a class
# Attribute: a variable bound to an instance of a class


class Kettle(object):

    power_source = "electric"

    # The difference between function and a method is that self parameter added to a method automatically
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.sale = False

    def sale_on(self):
        self.sale = True


kenwood = Kettle("Kenwood", 7.99)
print(kenwood.make)
print(kenwood.price)
print(kenwood.sale)

hamilton = Kettle("Hamilton", 16.99)
print(hamilton.make)
print(hamilton.price)
print(hamilton.sale)

kenwood.sale_on()
print(kenwood.sale)

Kettle.sale_on(hamilton)
print(hamilton.sale)

kenwood.color = "Red"
print(kenwood.color)

print(kenwood.power_source)
print(hamilton.power_source)


Kettle.power_source = "coal"
print(kenwood.power_source)
print(hamilton.power_source)

kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
