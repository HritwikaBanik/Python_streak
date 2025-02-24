m1='Make a lof of money'
m2 ='Buy Now'
m3 ='Subscribe this'
m4 ='Click this'

message = input("Enter your text :")

if (m1 in message) or (m2 in message) or (m3 in message) or (m4 in message):
    print("Spam detected")
else:
    print("No spams")