#the machine generates a random number and we have to guess it untill you find the right guess

from random import randint

c_guess = randint(1,100)
my_guess = -1
total_guesses = 0

while (c_guess != my_guess):
    total_guesses += 1
    my_guess = int(input("Enter your guess: "))
    if (c_guess == my_guess):
        print("Oh you guessed it right!")
    else:
        if(c_guess > my_guess):
            print("Lower guess please?")
        else:
            print("Higher guess please?")

print("You have guessed the number correctly in {} attempts ".format(total_guesses))
        
    