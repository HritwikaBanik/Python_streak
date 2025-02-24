a = int(input("Enter the number for its multiplication table:"))
for i in range(1, 11):
    print("{} * {} = {}".format(a, i, a * i))
    
    #using .format() because this is python 3.5 .f strings arentt introduced yet