n = int(input("Enter the number to find its factorial:"))

f= 1

for i in range(1,n+1):
    f = f * i

print("the factorial of {} is {}".format(n,f))
    