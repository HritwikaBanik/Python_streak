'''
****
***
**
*


'''

n = int(input("Enter the no of lines :"))

#recursive function

def pattern(n):
    if(n==0):
        return 
    else:
        print("*"*n)
        pattern(n-1)
    

pattern(n)