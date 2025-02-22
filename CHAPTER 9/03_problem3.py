def generateTable(i):
    # Generate the multiplication table for i (from 1 to 10)
    table = ""
    for n in range(1, 11):
        table += "{} x {} = {}\n".format(i, n, i * n)  # Format and append to table string
    
    # Define the folder path where the table will be saved
    folder_path = r"C:\Users\91600\Documents\GitHub\Algomagnet\Python_streak\CHAPTER 9\tables\table_{}.txt".format(i)
    
    # Write the table to the file
    with open(folder_path, "w") as f:
        f.write(table)

# Generate tables for numbers 2 to 20
for i in range(2, 21):
    generateTable(i)
