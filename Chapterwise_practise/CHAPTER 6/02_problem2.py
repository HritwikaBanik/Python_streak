marks1 = int(input("Enter marks of subject1: "))
marks2 = int(input("Enter marks of subject2: "))
marks3 = int(input("Enter marks of subject4: "))

percentage = (marks1+marks2+marks3)/3 * 100
print("percentage:",percentage)

if marks1>33 and marks2>33 and marks3>33:
    if percentage >= 40 :
        print("You are passed.")
    else:
        print("You failed.")
else:
    print("you failed.")