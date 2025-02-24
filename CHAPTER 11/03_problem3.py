class Employee:
    name = "Ram"
    salary = 39827
    increment = 20
    
    def __init__(self):
        pass
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))

# Create an instance of Employee
s = Employee()

# Access the salaryAfterIncrement property without parentheses
print(s.salaryAfterIncrement)
