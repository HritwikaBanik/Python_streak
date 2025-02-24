class animals:
    def __init__(self):
        pass
    
class pets(animals):
    def __init__(self):
        pass

class dogs(pets):
    def __init__(self):
        pass
        
    @staticmethod
    def bark():
        print("Thats how a dog barks.")


a = animals()
b = pets()
c = dogs()       
c.bark()
    