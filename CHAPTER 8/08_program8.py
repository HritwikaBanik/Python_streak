
n = int(input("Enter the number:"))

def multiplication_table(n):
    for i in range(1,11):
        print("{}x{}={}".format(i,n,n*i))
        
multiplication_table(n)