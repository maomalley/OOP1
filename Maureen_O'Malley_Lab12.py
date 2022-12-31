#A class named Car is created with the data attributes __year_model,
#__make and __speed.
class Car():
    #The __init__ method accepts arguments.
    def __init__(self, year, make, __speed):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    #The accelerate method adds 5 to the speed data attribute when called.
    def accelerate(self):
        self.__speed = self.__speed + 5

    #The brake method subtracts 5 from the speed data when called.
    def brake(self):
        self.__speed = self.__speed - 5

    #The get_speed method returns the current speed when called.
    def get_speed(self):
        return self.__speed

make = input("Enter the car's make: ")
year = int(input("Enter the car's year model: "))
__speed = 0

def main():
    myCar = Car(year, make, __speed)

    #The accelerate method is called 5 times and displays the current speed
    #each time that it is called.
    Car.accelerate(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.accelerate(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.accelerate(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.accelerate(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.accelerate(myCar)
    print("The current speed is",Car.get_speed(myCar))

    #The brake method is called 5 times and displays the current speed
    #each time that it is called.
    Car.brake(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.brake(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.brake(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.brake(myCar)
    print("The current speed is",Car.get_speed(myCar))
    Car.brake(myCar)
    print("The current speed is",Car.get_speed(myCar))
main()
