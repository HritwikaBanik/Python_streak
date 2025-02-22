import random
import os

def game():
    print("...Welcome to the Game...")

    # Generate a random score
    score = random.randint(1, 100)

    # Full path to the hiscore.txt file
    hiscore_file_path = r"C:\Users\91600\Documents\GitHub\Algomagnet\Python_streak\CHAPTER 9\hiscore.txt"
    
    # Check if the 'hiscore.txt' file exists
    if not os.path.exists(hiscore_file_path):
        # If not, create the file and set the high score to 0
        with open(hiscore_file_path, 'w') as f:
            f.write("0")

    # Fetch the score from the hiscore file
    with open(hiscore_file_path) as f:
        hiscore = f.read().strip()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    # Display the current score
    print("This is your current score: {}".format(score))

    # Check if the current score exceeds the high score
    if score > hiscore:
        print("Congratulations! You've set a new high score!")
        # Update the high score in the file
        with open(hiscore_file_path, 'w') as f:
            f.write(str(score))
    else:
        print("The high score is still: {}".format(hiscore))

    return

game()
