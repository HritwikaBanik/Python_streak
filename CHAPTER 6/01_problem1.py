a1 = int(input("Enter any number: "))
a2 = int(input("Enter any number: "))
a3 = int(input("Enter any number: "))
a4 = int(input("Enter any number: "))

if (a1>a2 and a1>a3 and a1>a4) :
    print( "greatest number: ",a1)
elif ( a1<a2 and a2>a3 and a2>a4) :
    print("greatest number:",a2)
elif ( a1<a3 and a2<a3 and a3>a4) :
    print("greatest number:",a3)
else:
    print("greatest number:",a4)