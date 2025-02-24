class TwoDVector:
    def __init__(self, i , j):
        self.i= i
        self.j =j
    def show(self):
        print("This is a 2D vector: {}i + {}j".format(self.i,self.j))
        
class ThreeDVector(TwoDVector):  #inheritence
    def __init__(self,k,i,j):
        super().__init__(i, j)
        self.k=k
    
    def show(self):
        print("This is a 3D vector: {}i + {}j + {}k".format(self.i,self.j,self.k))
    

a = TwoDVector(5,6)
a.show()
b =ThreeDVector(6,7,8)
b.show()