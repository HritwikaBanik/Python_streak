s = set()

s.add(18)  #integer

s.add("18") #string

s.add(18.0) #length of the is 2 .
print(s)

print(len(s))

'''In Python, 1 == 1.0 evaluates as True because Python automatically converts (or coerces) values to a common type for comparison, and in this case, 1 is an integer and 1.0 is a floating-point number. When comparing different numeric types, Python checks their values after converting both to the same type, which is usually the more general type (in this case, the float).

So, the integer 1 is automatically converted to 1.0 (a float), and the comparison becomes 1.0 == 1.0, which is obviously True.

This behavior is a part of Python's flexible handling of numeric types, aiming for ease of use in situations where numbers can be represented as either integers or floats.'''