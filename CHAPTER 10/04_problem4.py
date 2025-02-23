#create a calculate that can do square , cube , squareroot of any number

class Calculator:
    def __init__(self, number):
        self.number = number
    
    def square(self):
        #number is an instance variable. Since it's an instance variable, you should refer to it as self.number instead of just number.
        return self.number * self.number
    
    def cube(self):
        return self.number * self.number * self.number
    
    def squareroot(self):
        return self.number**(1/2)
    
    @staticmethod
    def hello():
        print("Hello buddy!")

# Take input from the user
n_value = float(input("Enter a number: "))

# Create an instance of Calculator with the user's input
n = Calculator(n_value)
n.hello()
print("Square of {} is {}".format(n.number, n.square()))
print("Cube of {} is {}".format(n.number, n.cube()))
print("Squareroot of {} is {}".format(n.number, round(n.squareroot(),2)))
