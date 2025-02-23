#create class "Programmer" for employees of Microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
        
employee = Programmer("Tina",20,2000000) #object/Instance
print(employee.name ,employee.age,employee.company)
employee = Programmer("Rina",30,2400000)
print(employee.name ,employee.age,employee.company)
print(employee.name ,employee.age,employee.company)
    