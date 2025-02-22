
n = int(input("Enter the no of natural numbers: "))


def sum_natural(n):
    if (n==1):
        return 1
    return sum_natural(n-1)+n

print("Total Sum is :",sum_natural(n))