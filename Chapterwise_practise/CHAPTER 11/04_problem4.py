#add two complex numbers 
#complex numbers have real part and imaginary part 

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    
    #adding complex numbers = real part + imaginary part
    def __add__(self,c2):
        return Complex(self.r + c2.r ,self.i + c2.i)
    
    def multiply(self, c2):
        real_part = (self.r * c2.r) - (self.i * c2.i)
        imaginary_part = (self.r * c2.i) + (self.i * c2.r)
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return "{} + {}i".format(self.r, self.i)
        
       
c = Complex(3,4)
d = Complex(5,7)
print( c + d)
product = c.multiply(d)
print(product)
        