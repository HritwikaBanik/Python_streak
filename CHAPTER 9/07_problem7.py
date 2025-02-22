file_path = r"C:\Users\91600\Documents\GitHub\Algomagnet\Python_streak\CHAPTER 9\log.html"

with open(file_path, "r") as f:
    lines = f.readlines()

lineno = 1   
for line in lines:
    if "python" in line.lower():  # Case-insensitive search
        print("Found in line no: {}".format(lineno))
        break
    lineno += 1    
else:
    print("Not found")

