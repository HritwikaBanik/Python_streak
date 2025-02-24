class Employee:
    name = "Ram"
    salary = 39827
    increment = 20
    
    def __init__(self):
        pass
    
    @property   #decorator
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))
    
    @salaryAfterIncrement.setter #setter function
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

# Create an instance of Employee
s = Employee()
print(s.salaryAfterIncrement)
# Access the salaryAfterIncrement property without parentheses
s.salaryAfterIncrement =44099
print(s.increment)

