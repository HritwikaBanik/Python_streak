c = int(input("Enter the temperature in Celcius:"))
#c/5 = (f-32)/9

def farenheit(c):
    return (c/5 * 9) + 32
    
print("The temperature in fahrenheit is:", farenheit(c))