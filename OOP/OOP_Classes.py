# Everything in python is an object
# OOP using Objects and Classes such as Methods
# When a function is part of a class, it is called a method
a = 12
b = 4
print(a + b)
print(a.__add__(b))

# A class is a template for which objects can be created


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)  # False
hamilton.switch_on()
print(hamilton.on)  # True

Kettle.switch_on(kenwood)
print(kenwood.on)  # True
kenwood.switch_on()

print("*" * 80)
kenwood.power = 1.5
print(kenwood.power)

print("Switch to atomic power")
Kettle.power_source = "Atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "Gas"
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)


