# copy of version of vehicle_2.py extended with additional class arguments for class Airplane

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
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)           # this allows us to inheretit the make and model from the Vehicle class
        self.faa_id = faa_id

    def FaaId(self):
        print('FAA ID: {self.faa_id}') 
    
    def moves(self):
        print('Flies along....')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along....')

# GolfCart is going to receive the same methods as the Vehicle class.
# There is no overwriting using values defined within the specific class (such as with Airplane(Vehicle) and Truck(Vehicle) classes)
class GolfCart(Vehicle):
   pass

airbus = Airplane('Airbus', 'A320', 'UHF124567')

airbus.get_make_model()
airbus.FaaId()
airbus.moves()



longbase = Truck('Ford', 'F-150')

longbase.get_make_model()
longbase.moves()

golfwagon = GolfCart('Toyota', 'Putt Putt')

golfwagon.get_make_model()
golfwagon.moves()

print('\n \n')

#polymorphism example
for vehicle in (my_car, fav_car, airbus, longbase, golfwagon):
    vehicle.get_make_model()
    vehicle.moves()