class Vector:
    def __init__(self, i, j, k):
        self.i = i  # i component
        self.j = j  # j component
        self.k = k  # k component
    
    # Adding vectors
    def __add__(self, V2):
        return (self.i + V2.i, self.j + V2.j, self.k + V2.k)
    
    # Dot product (scalar product)
    def __mul__(self, V2):
        return (self.i * V2.i + self.j * V2.j + self.k * V2.k)  # Dot product
    
    # Cross product (vector product)
    def cross(self, V2):
        i = self.j * V2.k - self.k * V2.j
        j = self.k * V2.i - self.i * V2.k
        k = self.i * V2.j - self.j * V2.i
        return Vector(i, j, k)

    # String representation for easy printing
    def __str__(self):
        return "{}i + {}j + {}k".format(self.i, self.j, self.k)

# Example Usage
v1 = Vector(1, 2, 3)  # Vector 1 (i=1, j=2, k=3)
v2 = Vector(4, 5, 6)  # Vector 2 (i=4, j=5, k=6)

# Dot product
dot_product = v1 * v2
print("Dot Product:", dot_product)

# Cross product
cross_product = v1.cross(v2)
print("Cross Product:", cross_product)
