class Vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    

# Example Usage
v1 = Vector([1, 2, 3])  # Vector 1 (i=1, j=2, k=3)
v2 = Vector([4, 5] )  # Vector 2 (i=4, j=5, k=6)

print(v1.__len__())
print(v2.__len__())

