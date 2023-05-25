## Unlimited positional arguments
def add(*args):
    summation = 0
    for n in args:
        summation += n
    return summation


print(add(3, 4, 5))



def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
my_car = Car(make = "Nissan", model="GT-R")
print(my_car.model)