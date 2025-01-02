class Vehicle():
# add an initializer method __init__ that takes two parameters: make and model
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print('Moves along....')

# add a getter method
    def get_make_model(self):
        print(f"I'm a {self.make}, {self.model} model.")


# we create an object from the class Vehicle
my_car = Vehicle('Kia', 'Cerato')

# create another object from the class Vehicle
fav_car = Vehicle('Mitsubishi', 'Outlander')
fav_car.moves()

# print options
# print(my_car.make)
# print(my_car.model)
# print(my_car.make, my_car.model)



# print(f"I'm a {my_car.make} {my_car.model}")

#using the getter method we now just call the method to execute the print statement
my_car.get_make_model()

# we call the method moves() on the object my_car
my_car.moves()

# now we call the method to get our print output
fav_car.get_make_model()
fav_car.moves()

# the class Airplane is going to receive the same methods as the Vehicle class. 
# This is called inheritance. Inheritance allows us to reuse code and create new classes based on existing ones.
class Airplane(Vehicle):
    def moves(self):
        print('Flies along....')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along....')

# GolfCart is going to receive the same methods as the Vehicle class.
# There is no overwriting using values defined within the specific class (such as with Airplane(Vehicle) and Truck(Vehicle) classes)
class GolfCart(Vehicle):
   pass

airbus = Airplane('Airbus', 'A320')

airbus.get_make_model()
airbus.moves()

longbase = Truck('Ford', 'F-150')

longbase.get_make_model()
longbase.moves()

golfwagon = GolfCart('Toyota', 'Putt Putt')

golfwagon.get_make_model()
golfwagon.moves()
